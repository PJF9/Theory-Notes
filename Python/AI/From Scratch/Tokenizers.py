from collections import defaultdict
from tqdm import tqdm
import json
from math import log
from copy import deepcopy


class WordPiece:
    """
    Its O(n) with respect both the `ntokens` and the total documents of `corpus`.
    """
    def __init__(self, corpus=None, ntokens=30_000, cleaning=None):
        if (corpus is not None):
            # Cleaning Corpus
            if (cleaning is not None):
                corpus = [cleaning(text) for text in corpus]

            # Calculating the frequencies of each word (global statistics)
            self._word_freqs = defaultdict(lambda : 0)
            for text in corpus:
                for word in text.split():
                    self._word_freqs[word] += 1

        self._cleaning = cleaning if (cleaning is not None) else lambda text: text
        self._ntokens = ntokens
        self.special_t = ["[CLS]", "[UNK]", "[PAD]", "[SEP]"]
        self.vocab_l = []
        self.vocab_d = {}
        self.ivocab_d = {}
        self.vocab_size = 0
    

    def __calc_pair_scores(self, splits):
        token_freqs = defaultdict(lambda: 0)  # Capturing the global corpus statistics for `freq of firsy element` and `freq of second element`
        pair_freqs = defaultdict(lambda: 0)   # Capturing the statistics for `freq of pair`: How many times this pair appears in the corpus

        # Iterate over all words of the corpus
        for word, freq in self._word_freqs.items():
            split = splits[word]

            # If a word contains only 1 letter
            if len(split) == 1:
                token_freqs[split[0]] += freq
                continue

            for i in range(len(split) - 1):
                token_freqs[split[i]] += freq
                pair_freqs[(split[i], split[i+1])] += freq

            # Adding the final token that the for-loop is not processing
            token_freqs[split[-1]] += freq

        # Returning the scores, calculated from the formula above
        return {pair: pair_freq / (token_freqs[pair[0]] * token_freqs[pair[1]]) for pair, pair_freq in pair_freqs.items()}


    @staticmethod
    def __highest_score(pair_scores):
        max_pair = ('', '')
        max_freq = 0
        for pair, freq in pair_scores.items():
            if freq > max_freq:
                max_freq = freq
                max_pair = pair
        
        return max_pair, max_freq
    
    @staticmethod
    def __merge_pair(pair_tuple, splits):
        # Iterating over the word-tokens defaultdict
        for word in splits.keys():
            split = splits[word] # contains the tokens of the word

            if len(split) == 1:
                continue
            
            # Iterating until we find the pair in the tokenize representation of the word
            i = 0
            while i < len(split) - 1:
                if (split[i] == pair_tuple[0]) and (split[i+1] == pair_tuple[1]):
                    merge = pair_tuple[0] + pair_tuple[1][2:] if pair_tuple[1].startswith("##") else pair_tuple[0] + pair_tuple[1]
                    split = split[:i] + [merge] + split[i+2:]
                else:
                    i += 1

            splits[word] = split
        return splits
    

    def fit(self):
        # Original splits (character tokenization of each word in the corpus)
        splits = {word: [c if i == 0 else f"##{c}" for i, c in enumerate(word)] for word in self._word_freqs.keys()}

        # Creating the basic vocabulary
        vocab_ = set([token for tokens in splits.values() for token in tokens])
        
        new_tokens = []
        for _ in tqdm(range(len(vocab_), self._ntokens), desc="Creating Vocabulary: "):
            ps = self.__calc_pair_scores(splits)   # Calculate the Score of each pair
            bs, _ = self.__highest_score(ps)       # Get the pair with the highest score
            splits = self.__merge_pair(bs, splits) # Merge those two tokens

            if bs[1].startswith("##"):
                new_tokens.append(bs[0] + bs[1][2:])
                continue
            new_tokens.append(bs[0] + bs[1])

        # Adding to the the basic vocabulary the new tokens
        self.vocab_l = self.special_t + sorted(list((vocab_ | set(new_tokens))))
        self.vocab_d = {term: i for i, term in enumerate(self.vocab_l)}
        self.ivocab_d = {i: term for i, term in enumerate(self.vocab_l)}
        self.vocab_size = len(self.vocab_l)

    
    def save_vocab(self, path):
        # Saving the Vocabulary Dict into a JSON file
        with open(path, "w") as f:
            json.dump(self.vocab_d, f)

    def load_vocab(self, path):
        # Updating the Vocabulary elements from the JSON file
        with open(path, "r") as f:
            self.vocab_d = json.loads(f.read())
        self.vocab_l = list(self.vocab_d.keys())
        self.ivocab_d = {i: token for i, token in enumerate(self.vocab_l)}
        self.vocab_size = len(self.vocab_l)


    def __tokenize_word(self, word):
        tokens = []

        # Iterating over the entire word starting from the end
        while len(word) > 0:
            i = len(word)
            # Trying to find the bigest sub-word that exists on our vocabulary
            while (i > 0) and word[:i] not in self.vocab_l:
                i -= 1

            # If a sub-word does not exist on the vocabulary
            if i == 0:
                tokens.append("[UNK]")
                return tokens          # keeping some information about the word
            
            # The first sub-word is not going to contain `##`
            tokens.append(word[:i])
            word = word[i:]

            # All the other sub-words are going to contain `##`
            if len(word) > 0:
                word = f"##{word}"

        return tokens
    
    def __decode_word(self, idx):
        to_tokens = [self.ivocab_d[i] for i in idx]

        return ''.join([token[2:] if token.startswith("##") else token for token in to_tokens])


    def tokenize(self, text, npad=0):
        t_text = []
        for word in self._cleaning(text).split():
            for token in self.__tokenize_word(word):
                t_text.append(token)
            t_text.append("[SEP]")

        for _ in range(npad - len(t_text)):
            t_text.append("[PAD]")

        return t_text

    def encode(self, text, npad=0):
        return [self.vocab_d[token] for token in self.tokenize(text, npad=npad)]

    def decode(self, idx):
        text = ""
        i, j = 0, 0
        while i < len(idx) and idx[i] != self.vocab_d["[PAD]"]:
            if idx[i] == self.vocab_d["[SEP]"]:
                text += self.__decode_word(idx[j: i]) + " "
                j = i + 1
            i += 1

        return text


class Unigram:
    def __init__(self, corpus=None, ntokens=30_000, cleaning=None, mult=None):
        if (corpus is not None):
            # Cleaning Corpus
            if (cleaning is not None):
                corpus = [cleaning(text) for text in corpus]

            # Calculating the frequencies of each word (global statistics)
            self._word_freqs = defaultdict(lambda : 0)
            for text in corpus:
                for word in text.split():
                    self._word_freqs[word] += 1

            self._ntokens = ntokens # `self.__basic_vocab()` needs `ntokens`
            mult = mult if mult is not None else 3
            self._token_freqs = self.__basic_vocab(mult)
            self._model = {token: -log(freq / sum(self._token_freqs.values())) for token, freq in self._token_freqs.items()}

        self._cleaning = cleaning if (cleaning is not None) else lambda text: text
        self._ntokens = ntokens
        self.special_t = ["[CLS]", "[UNK]", "[PAD]", "[SEP]"]
        self.vocab_l = []
        self.vocab_d = {}
        self.ivocab_d = {}
        self.vocab_size = 0


    def __basic_vocab(self, mult):
        char_freq = defaultdict(lambda : 0)
        subs_freq = defaultdict(lambda : 0)

        for word, freq in self._word_freqs.items():
            for i in range(len(word)):
                char_freq[word[i]] += freq # updating chracter frequency

                for j in range(i+2, len(word) + 1): # we need to contain `len(word)` because `slice` does not contain `end index`.
                    subs_freq[word[i:j]] += freq    # updating substring frequency
        
        # Sorting Sub-String Tokens
        sorted_subs = sorted(subs_freq.items(), key=lambda x: x[1], reverse=True)

        # Concatenating those 2 token sets
        token_freq = list(char_freq.items()) + sorted_subs[: int(mult * self._ntokens)]

        return dict(token_freq)

    @staticmethod
    def __best_segmentations(word, model):
        # Contains starting character index of the best word segmentations that ends in this particular index
        best_segmentations = [{"start": 0, "score": 0}] + [{"start": None, "score": None} for _ in range(len(word))] # adding one more element for efficiency

        for start_idx in range(len(word)):
            best_score_at_start = best_segmentations[start_idx]["score"] # initially is 0, but then: `{"start": start_idx, "score": score}`

            for end_idx in range(start_idx + 1, len(word) + 1):
                token = word[start_idx: end_idx]

                if (token in model) and (best_score_at_start is not None):
                    score = model[token] + best_score_at_start

                    # If we have found a better segmentation ending at `end_idx``, we update
                    if (best_segmentations[end_idx]["score"] is None) or (best_segmentations[end_idx]["score"] > score):
                        best_segmentations[end_idx] = {"start": start_idx, "score": score}

        return best_segmentations


    def __segment_word(self, word, model):
        best_segmentations = self.__best_segmentations(word, model) # contains the starting indexes of the best segmentation ending at each character position
        segmentation = best_segmentations[-1]               # contains the index and the score of the best segmentation ending at the last character

        if segmentation["score"] is None: return (["[UNK]"], None) # If the mode cannot segment the word, due to OOV

        score = segmentation["score"] # the score of the best segmentation ending at the last `word` character
        start = segmentation["start"] # the starting index of the best segmentation ending at the last `word` character
        end = len(word)
        tokens = []

        # Calculating the best segmentation
        while start != 0:
            tokens.insert(0, word[start: end])
            start, end = best_segmentations[start]["start"], start # start -> the index of the best segmentation ending at `end` | end -> start, we have segment the word from end to start
        
        tokens.insert(0, word[start: end]) # adding the last segment to the list

        return (tokens, score)


    def __get_loss(self, model):
        l = 0
        for word, freq in self._word_freqs.items():
            _, word_loss = self.__segment_word(word, model)
            l += (freq * word_loss)

        return l
    
    def __get_scores(self, _model):
        scores = {}
        model_loss = self.__get_loss(_model)

        for token in _model.keys():
            if len(token) == 1: # preventing the model for deleting character-level tokens
                scores[token] = float("inf")

            else:
                model_without_token = deepcopy(_model)
                model_without_token.pop(token) # removing the token from the model - Dictionary

                scores[token] = self.__get_loss(model_without_token) - model_loss

        return scores
    

    def fit(self, p_rem=0.1):
        while len(self._model) > self._ntokens:
            # Calculating scores and sorting them from lower to higher
            scores = sorted(self.__get_scores(self._model).items(), key=lambda x: x[1])

            # Removing the percentage specified of low-scored tokens
            for i in range(int(len(self._model) * p_rem)):
                self._token_freqs.pop(scores[i][0])

            # Initializing the new model
            self._model = {token: -log(freq / sum(self._token_freqs.values())) for token, freq in self._token_freqs.items()}

        self.vocab_l = self.special_t + sorted(list(self._token_freqs.keys()))
        self.vocab_d = {term: i for i, term in enumerate(self.vocab_l)}
        self.ivocab_d = {i: term for i, term in enumerate(self.vocab_l)}
        self.vocab_size = len(self.vocab_l)

    def save_vocab(self, path):
        # Saving the Vocabulary Dict into a JSON file
        with open(path, "w") as f:
            json.dump(self.vocab_d, f)

    def load_vocab(self, path):
        # Updating the Vocabulary elements from the JSON file
        with open(path, "r") as f:
            self.vocab_d = json.loads(f.read())
        self.vocab_l = list(self.vocab_d.keys())
        self.ivocab_d = {i: token for i, token in enumerate(self.vocab_l)}
        self.vocab_size = len(self.vocab_l)


    def tokenize(self, text, npad=0):
        tokenized_text = []

        for word in self._cleaning(text).split():
            tokenized_text.append(self.__segment_word(word, self._model)[0])
            tokenized_text.append(["[SEP]"])

        for _ in range(npad - len(tokenized_text)):
            tokenized_text.append(["[PAD]"])

        return sum(tokenized_text, []) # starting from [] and adding elements from the `tokenized_text`
    
    def encode(self, text, npad=0):
        return [self.vocab_d[token] for token in self.tokenize(text, npad=npad)]
    
    def __decode_word(self, idx):
        return ''.join([self.ivocab_d[i] for i in idx])

    def decode(self, idx):
        text = ""
        i, j = 0, 0
        while i < len(idx) and idx[i] != self.vocab_d["[PAD]"]:
            if idx[i] == self.vocab_d["[SEP]"]:
                text += self.__decode_word(idx[j: i]) + " "
                j = i + 1
            i += 1

        return text
