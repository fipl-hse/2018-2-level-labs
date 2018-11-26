"""
Labour work #3
 Building an own N-gram model
"""

import re
import math
from typing import List

if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


def split_by_sentence(text: str) -> list:
    if not text:
        return []

    '''abc = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for a in abc:
        if a not in text:
            return []'''

    if ' ' not in text:
        return []

    text = text.replace('\n', '')
    text = re.sub(r'[`~@#$%^&*+=\']', '', text)

    # split by sentence
    text_sentences = re.split(r'[.?!]+ ', text)

    # split by word
    list_tokens = []
    for sentence in text_sentences:
        token = re.split(r'\W+', sentence)
        list_tokens.append(token)

    # delete last empty list
    for sentence in list_tokens:
        while '' in sentence:
            sentence.remove('')

    # add <s> </s>
    for sentence in list_tokens:
        sentence.insert(0, '<s>')
    for sentence in list_tokens:
        sentence.append('</s>')

    # make lower
    list_tokens_clear = []
    for sentence in list_tokens:
        new_sentence = [token.lower() for token in sentence]
        list_tokens_clear.append(new_sentence)

    print(list_tokens_clear)
    return list_tokens_clear


split_by_sentence('Mar#y wa$nted, to swim! \n However, she was afraid of sharks.')


class WordStorage:

    def __init__(self):
        self.storage = {}
        self.word_id = 0

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return {}
        if word is None:
            return None
        if word in self.storage.keys():
            return self.storage[word]

        self.storage[word] = self.word_id
        self.word_id += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.storage.keys():
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return 'UNK'
        for word, word_id in self.storage.items():
            if word_id == id:
                return word

    def from_corpus(self, corpus: tuple):
        if corpus is None:
            return ()
        if isinstance(corpus, str):
            return -1
        for word in corpus:
            self.put(word)


class NGramTrie:

    # bi-grams

    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'ERROR'
        if sentence == ():
            return ''
        size = self.size
        counter = 0
        n_grams = []
        while counter != len(sentence) - size + 1:
            n_grams.append(sentence[counter:counter + size])
            counter += 1
        for el in n_grams:
            frequency = n_grams.count(el)
            self.gram_frequencies[el] = frequency
        return 'OK'

    def calculate_log_probabilities(self):
        for gram, freq in self.gram_frequencies.items():
            probability = 0
            for another_gram, another_freq in self.gram_frequencies.items():
                if gram[0] == another_gram[0]:
                    probability += another_freq
                else:
                    continue
            gram_probability = freq / probability
            gram_log_probability = math.log(gram_probability)
            self.gram_log_probabilities[gram] = gram_log_probability

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple):
            return []
        if len(prefix) > 1:
            return []

        prefix_list = list(prefix)
        while True:
            ngrams = []
            for gram in self.gram_log_probabilities:
                if gram[0] == prefix[0]:
                    ngrams.append((self.gram_log_probabilities[gram], gram))
            if ngrams != []:
                prefix = ((max(ngrams)[1])[1],)
                prefix_list.append(prefix[0])
                ngrams.append(prefix)
            else:
                return prefix_list

def encode(storage_instance, corpus) -> list:
    encoded_sentences = []
    for sentence in corpus:
        encoded_sentence = []
        for word in sentence:
            code_word = storage_instance.get(word)
            encoded_sentence += [code_word]
        encoded_sentences += [encoded_sentence]
    return encoded_sentences
