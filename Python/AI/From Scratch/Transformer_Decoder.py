import torch
from torch import nn
from torch.nn import functional as F
from torchinfo import summary


### Problem: Learn how to generate text base on all Shakespeare's plays.
### Tokenization: Character


### Hyperparameters
BATCH_SIZE = 64         # the size of sample (in our case character tokens) to create batches 
BLOCK_SIZE = 256        # the context length (the tokens that each batch will contain): using Attention those tokens are able to communicate
EMBED_SIZE = 384        # the size of the embeddings for each token
EPOCHS = 4_000          # the number of times we iterate all the batches in training
LR = 3e-4               # the learning rate of the optimizer: in our case AdamW
EVAL_INTERVAL = 400     # every after those epochs we are evaluating the loss of the model
EVAL_ITERS = 200        # for how many batches we should calculate the loss when evaluating the model
NUM_HEADS = 6           # the number of Masked Self-Attention layers
NUM_LAYERS = 6          # the number of Block Layer (each Block contains one Mulit-Head Attention and one Feed-Forward layer)
DROPOUT = 0.2           # the dropout we are setting in the layers
SCALE_EMBEDS = 4        # how many times we want to scale the embedding dimension in the Feed-Froward layer


### Setting Devide Agnostic Code
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


### Loading the Dataset
with open("Shakespeare_plays.txt", "r") as f:
    text_ds = f.read()


### Creating Vocabulary and Encoder/Decoder Functions
vocab = sorted(list(set(text_ds)))
vocab_size = len(vocab)

char_to_int = {ch: i for i, ch in enumerate(vocab)}
int_to_char = {i: ch for i, ch in enumerate(vocab)}
encoder = lambda s: [char_to_int[c] for c in s]
decoder = lambda l: "".join([int_to_char[i] for i in l])


### Tokenizing the Dataset
tokenized_ds = torch.tensor(encoder(text_ds), dtype=torch.long, device=device) # `torch.int64`


### Splitting the Dataset into Training and Validation Sets
train_size = int(len(tokenized_ds) * 0.9)
train_data, valid_data = tokenized_ds[:train_size], tokenized_ds[train_size:]


### Splitting the Dataset into Batches
def get_batch(split):
    data = train_data if split == "train" else valid_data

    # Creating random indexes for computing the batches
    idx_xb = torch.randint(len(data) - BLOCK_SIZE, (BATCH_SIZE,))

    x = torch.stack([data[i:BLOCK_SIZE+i] for i in idx_xb])
    y = torch.stack([data[i+1:BLOCK_SIZE+i+1] for i in idx_xb])

    return x.to(device=device, non_blocking=True), y.to(device=device, non_blocking=True)


### Creating a Loss Calculation Function
@torch.inference_mode()
def estimate_loss(model):
    out = {}

    model.eval()
    for split in ["train", "valid"]:
        losses = torch.zeros(EVAL_ITERS)

        # Iterate `EVAL_ITERS` number of times to reduce the noice that each batch contains
        for i in range(EVAL_ITERS):
            xb, yb = get_batch(split)
            _, loss = model(xb, yb)
            losses[i] = loss.item()
        
        out[split] = losses.mean()
    
    model.train()
    return out


class SelfAttentionMasked(nn.Module):
    def __init__(self, head_size):
        super().__init__()

        # Initializing the query, key and value vectors
        self.key = nn.Linear(EMBED_SIZE, head_size, bias=False)
        self.query = nn.Linear(EMBED_SIZE, head_size, bias=False)
        self.value = nn.Linear(EMBED_SIZE, head_size, bias=False)

        # Creating a variable `tril` that is not a parameter
        self.register_buffer("tril", torch.tril(torch.ones(BLOCK_SIZE, BLOCK_SIZE)))

        self.dropout = nn.Dropout(DROPOUT)

    def forward(self, x):
        # Capturing the input dimensions: (B: `batch`, T: `time`, C: `channels`) = (BATCH_SIZE, BLOCK_SIZE, EMBED_SIZE)
        _, _, C = x.shape

        # Calculate key and query
        k = self.key(x)   # (B, T, head_size)
        q = self.query(x) # (B, T, head_size)
        
        # Calculating the weight matrix that captures the connections of the tokens: (B, T, head_size) @ (B, head_size, T) --> (B, T, T)
        wei = q @ k.transpose(-2, -1) * C**-0.5               # 1. Where a single query token needs to give more attention in the key tokens
        wei = wei.masked_fill(self.tril == 0, float("-inf"))  # 2. Masking the attention matrix to hide the future tokens (of a token)
        wei = F.softmax(wei, dim=-1)                          # 3. Converting the attention matrix into probabilities

        wei = self.dropout(wei)

        # Calculate value to determine how much each token want each token is ready to communicate with the other tokens
        v = self.value(x)

        out = wei @ v # (B, T, T) @ (B, T, head_size) --> (B, T, head_size)

        return out
    

class MultiHeadAttentionMasked(nn.Module):
    def __init__(self, head_size):
        super().__init__()

        self.heads = nn.ModuleList([SelfAttentionMasked(head_size) for _ in range(NUM_HEADS)])
        self.proj = nn.Linear(EMBED_SIZE, EMBED_SIZE)
        self.dropout = nn.Dropout(DROPOUT)

    def forward(self, x):
        # Contatenate the outputs of each Masked Self-Attention
        out = torch.cat([head(x) for head in self.heads], dim=-1) # (B, T, EMBED_SIZE)
        out = self.dropout(self.proj(out))
        return out


class FeedForward(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(EMBED_SIZE, SCALE_EMBEDS * EMBED_SIZE),
            nn.ReLU(),
            nn.Linear(SCALE_EMBEDS * EMBED_SIZE, EMBED_SIZE),
            nn.Dropout(DROPOUT)
        )

    def forward(self, x):
        return self.net(x) # (B, T, EMBED_SIZE)
    

class Block(nn.Module): # combining Masked Multi-Head Attention and one Feed-Forward layer
    def __init__(self):
        super().__init__()

        head_size = EMBED_SIZE // NUM_HEADS # because the result of the Masked Multi-Head layer we want to have shape: (B, T, EMBED_SIZE)
        self.multi_att_m = MultiHeadAttentionMasked(head_size=head_size)
        self.ffwd = FeedForward()
        self.ln1 = nn.LayerNorm(EMBED_SIZE)
        self.ln2 = nn.LayerNorm(EMBED_SIZE)

    def forward(self, x): 
        x = x + self.multi_att_m(self.ln1(x)) # (B, T, EMBED_SIZE)
        x = x + self.ffwd(self.ln2(x))        # (B, T, EMBED_SIZE)

        return x


class TransformerDecoder(nn.Module):
    def __init__(self):
        super().__init__()

        self.embedding_table = nn.Embedding(vocab_size, EMBED_SIZE)
        # Self-Attention doesn't take into consideration the position of tokens when computing the attetnion matrix, so we have to
        self.position_embedding_table = nn.Embedding(BLOCK_SIZE, EMBED_SIZE)
        self.block = nn.Sequential(*[Block() for _ in range(NUM_LAYERS)])
        self.ln_f = nn.LayerNorm(EMBED_SIZE)
        self.linear_head = nn.Linear(EMBED_SIZE, vocab_size)        

    def forward(self, idx, targets=None):
        token_embeddings = self.embedding_table(idx)                                                   # (B, T, EMBED_SIZE)
        position_embeddings = self.position_embedding_table(torch.arange(BLOCK_SIZE, device=device)) # (T, EMBED_SIZE)

        x = token_embeddings + position_embeddings # (B, T, EMBED_SIZE)

        x = self.block(x) # (B, T, EMBED_SIZE)
        x = self.ln_f(x)  # (B, T, EMBED_SIZE)

        logits = self.linear_head(x) # (B, T, vocab_size)
        
        # Condition to seperate training and generating phase
        if targets is None:
            loss = None
        else:
            logits = logits.view(BATCH_SIZE*BLOCK_SIZE, vocab_size)
            targets = targets.view(BATCH_SIZE*BLOCK_SIZE)

            loss = F.cross_entropy(logits, targets) # expects: (B*T, vocab_size) as logit tensor

        return logits, loss

    @torch.inference_mode()
    def generate(self, idx, max_new_tokens):
        self.eval()
        for _ in range(max_new_tokens):
            # Due to positional embeddings is only rational to pass T size of character tokens into the model
            idx_cond = idx[:, -BLOCK_SIZE:] # conditioning the input in order for each generation to consider the last T characters

            logits, _ = self(idx_cond) # (B, T, vocab_size)
    
            # We want the output of the last time step to generate the next
            logits = logits[:, -1, :] # (B, vocab_size)

            probs = F.softmax(logits, dim=1) # (B, vocab_size)

            # For each batch getting the index of the highest probability (using multinomial distribution)
            idx_next = torch.multinomial(probs, num_samples=1) # (B, 1)

            idx = torch.cat((idx, idx_next), dim=1) # (B, T+1)

        self.train()
        return idx
    

### Initializing the Model
model = TransformerDecoder().to(device)


### Printing the Model Structure
summary(model=model,
        input_size=(1, BLOCK_SIZE),
        col_names=["input_size", "output_size", "num_params", "trainable"],
        device=device,
        dtypes=[torch.long])


### Setting Optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=LR)


### Training the Model
print("\nStarting Training:")
for epoch in range(1, EPOCHS+1):
    # Evaluating Loss every EVAL_INTERVAL
    if epoch % EVAL_INTERVAL == 0:
        losses = estimate_loss(model)
        print(f"\nEpoch: {epoch} | Training Loss: {losses['train']: .4f} | Validation Loss: {losses['valid']: .4f}")

    xb, yb = get_batch("train")

    logits, loss = model(xb, yb)

    # Performing backpropagation and gradient descent
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()


### Generating Text (exactly 1_000 characters)
idx = torch.zeros((1, 1), dtype=torch.long, device=device)

with open("test.txt", "w") as f:
    f.write(decoder(model.generate(idx, max_new_tokens=1_000)[0].tolist()))
