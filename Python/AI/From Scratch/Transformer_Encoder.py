import torch
from torch import nn
from torch.nn import functional as F
from torchinfo import summary

import pandas as pd

from tqdm import tqdm


### Problem: Learn to identify spam sequences base on the sms dataset
### Tokenization: Character


### Hyperparameters
BATCH_SIZE = 32         # the size of sample (in our case character tokens) to create batches 
EMBED_SIZE = 300        # the size of the embeddings for each token
EPOCHS = 500          # the number of times we iterate all the batches in training
LR = 3e-4               # the learning rate of the optimizer: in our case AdamW
EVAL_INTERVAL = 50     # every after those epochs we are evaluating the loss of the model
EVAL_ITERS = 5        # for how many batches we should calculate the loss when evaluating the model
NUM_HEADS = 6           # the number of Masked Self-Attention layers
NUM_LAYERS = 6          # the number of Block Layer (each Block contains one Mulit-Head Attention and one Feed-Forward layer)
DROPOUT = 0.2           # the dropout we are setting in the layers
SCALE_EMBEDS = 4        # how many times we want to scale the embedding dimension in the Feed-Froward layer


### Setting Devide Agnostic Code
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


### Loading the Dataset into DataFrame Format
df = pd.read_csv("sms_spam.csv", encoding="latin-1")[["v1", "v2"]] # By default there are another 2 columns that doe't have data
df.rename(columns={"v1": "num_label", "v2": "raw_text"}, inplace=True)


### Creating the Vocabulary (we denote [CLS] as '{' and [PADD] as '}')
vocab = sorted(list(set(c for s in df["raw_text"] for c in s)) + ['{'] + ['}'])
vocab_size = len(vocab)


### Creating Encoder and Decoder Functions
char_to_int = {ch: i for i, ch in enumerate(vocab)}
int_to_char = {i: ch for i, ch in enumerate(vocab)}
encoder = lambda s: [char_to_int[c] for c in s]
decoder = lambda l: "".join([int_to_char[i] for i in l])


### Getting the maximum length of the raw text messages
max_sentence_length = df["raw_text"].str.len().max()


### Preprocessing the Dataset:
# 1. Convert the labels from "ham", "spam" into [1, 0] and [0, 1] respectively
# 2. Add the [CLC] and [PADD] tokens
# 3. Tokenize the text
df["label"] = df["num_label"].map({"ham": [1, 0], "spam": [0, 1]})
df["proc_text"] = df["raw_text"].apply(lambda l: "{" + l + "".join(["}" for _ in range(max_sentence_length - len(l))]))
df["tokenized_text"] = df["proc_text"].apply(encoder)

max_sentence_length += 1 # Due to the [CLC] token


### Splitting the Dataset into Training and Validation Sets
train_size = int(len(df) * 0.9)
train_ds, valid_ds = df.iloc[:train_size], df.iloc[train_size:].reset_index(drop=True) # don't add the previous indexes as a new column


### Creating the Function that Splits the Dataset into Batches
def get_batch(split=None):
    data = train_ds if split == "train" else valid_ds

    idx_xb = torch.randint(len(data), (BATCH_SIZE,)) # Random indexes from the Dataset

    x = torch.stack([torch.tensor(data["tokenized_text"][i.item()], dtype=torch.long) for i in idx_xb])
    y = torch.tensor([data["label"][i.item()] for i in idx_xb], dtype=torch.long)    

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


### Creating the Model
class SelfAttention(nn.Module):
    def __init__(self, head_size):
        super().__init__()

        self.query = nn.Linear(EMBED_SIZE, head_size, bias=False)
        self.key = nn.Linear(EMBED_SIZE, head_size, bias=False)
        self.value = nn.Linear(EMBED_SIZE, head_size, bias=False)

        self.dropout = nn.Dropout(DROPOUT)

    def forward(self, x):
        _, _, C = x.shape # B: BATCH_SIZE, T: max_sentence_length, C: head_size

        q = self.query(x) # (B, T, C)
        k = self.key(x)   # (B, T, C)

        wei = q @ k.transpose(-2, -1) * (C**-0.5) # (B, T, C) @ (B, C, T) --> (B, T, T)
        wei = F.softmax(wei, dim=-1)
        wei = self.dropout(wei)

        v = self.value(x) # (B, T, C)

        out = wei @ v # (B, T, T) @ (B, T, C) --> (B, T, C)

        return out
    

class MultiHeadAttention(nn.Module):
    def __init__(self, head_size):
        super().__init__()

        self.heads = nn.ModuleList([SelfAttention(head_size) for _ in range(NUM_HEADS)])
        self.proj = nn.Linear(EMBED_SIZE, EMBED_SIZE, DROPOUT)
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
        self.multi_att_m = MultiHeadAttention(head_size)
        self.ffwd = FeedForward()
        self.ln1 = nn.LayerNorm(EMBED_SIZE)
        self.ln2 = nn.LayerNorm(EMBED_SIZE)

    def forward(self, x): 
        x = x + self.multi_att_m(self.ln1(x)) # (B, T, EMBED_SIZE)
        x = x + self.ffwd(self.ln2(x))        # (B, T, EMBED_SIZE)

        return x
    

class TransformerEncoder(nn.Module):
    def __init__(self):
        super().__init__()

        self.embedding_table = nn.Embedding(vocab_size, EMBED_SIZE)
        self.position_embedding_table = nn.Embedding(max_sentence_length, EMBED_SIZE)

        self.block = nn.Sequential(*[Block() for _ in range(NUM_LAYERS)])
        self.ln_f = nn.LayerNorm(EMBED_SIZE)
        self.linear_head = nn.Linear(EMBED_SIZE, 2)        

    def forward(self, idx, targets=None):
        token_embeddings = self.embedding_table(idx)                                                 # (B, T, EMBED_SIZE)
        position_embeddings = self.position_embedding_table(torch.arange(max_sentence_length, device=device)) # (T, EMBED_SIZE)

        x = token_embeddings + position_embeddings # (B, T, EMBED_SIZE)

        x = self.block(x) # (B, T, EMBED_SIZE)
        x = self.ln_f(x)  # (B, T, EMBED_SIZE)

        logits = self.linear_head(x) # (B, T, 2)

        # Condition to seperate training and generating phase
        loss = F.cross_entropy(logits[:, 0, :], targets.float()) if targets is not None else None

        return logits, loss

    @torch.inference_mode()
    def predict(self, idx):
        self.eval()

        # Adding batch dimension for individual predictions
        if idx.dim() == 1:
            idx = idx.unsqueeze(dim=0)

        logits, _ = self(idx)
        probs = F.softmax(logits, dim=-1)

        self.train()

        return [{"Ham": probs[i][0][0].item(), "Spam": probs[i][0][1].item()} for i in range(idx.shape[0])]


### Initializing the Model
model = TransformerEncoder().to(device)


### Printing the Model Structure
summary(model=model,
        input_size=(1, max_sentence_length),
        col_names=["input_size", "output_size", "num_params", "trainable"],
        device=device,
        dtypes=[torch.long])


### Setting Optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=LR)


### Training the Model
print("\nStarting Training:")
for epoch in tqdm(range(1, EPOCHS+1)):
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


### Making Predictions
xb, yb = get_batch()

for i in range(BATCH_SIZE):
    x_first_sample, y_first_sample = xb[i], yb[i]

    print(decoder(x_first_sample.tolist()).split('}')[0][1:])
    print(model.predict(x_first_sample))
    print(y_first_sample.tolist())
    print()
