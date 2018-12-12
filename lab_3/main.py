"""
Labour work #3
 Building an own N-gram model
"""
from math import log
import re
REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:

    def __init__(self):
        self.indicator = 0
        self.storage = {}

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word in self.storage.keys():
            return self.storage[word]

        self.storage[word] = self.indicator
        self.indicator += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
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
        if not isinstance(corpus, tuple):
            return 'Error'

        for word in corpus:
            self.put(word)
        return 'OK'


class NGramTrie:

    def __init__(self, dimension: int):
        self.size = dimension
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'Error'
        if sentence == ():
            return ''

        dimension = self.size
        meter = 0
        n_grams = []
        while meter != len(sentence) - dimension + 1:
            n_grams.append(sentence[meter:meter + dimension])
            meter += 1
        for e in n_grams:
            frequency = n_grams.count(e)
            self.gram_frequencies[e] = frequency
        return 'OK'

    def calculate_log_probabilities(self):
        for gram, freq in self.gram_frequencies.items():
            all_probability = 0
            for _gram, _freq in self.gram_frequencies.items():
                if gram[0] == _gram[0]:
                    all_probability += _freq
                else:
                    continue
            gram_probability = freq / all_probability
            gram_log_probabilities = log(gram_probability)
            self.gram_log_probabilities[gram] = gram_log_probabilities
        return 'OK'

    def predict_next_sentence(self, prefix: tuple) -> list:
        if (not isinstance(prefix, tuple)) or (len(prefix) != self.size - 1) or (self.gram_log_probabilities == {}):
            return []
        predicted_sentence = list(prefix)
        length = 0
        while length != len(predicted_sentence):
            length = len(predicted_sentence)
            for key, value in sorted(self.gram_log_probabilities.items(), key=lambda item: -item[1]):
                keys = list(key)
                if keys[:-1] == predicted_sentence[-(self.size - 1):]:
                    predicted_sentence.append(key[-1])
                    break
        return predicted_sentence


def encode(storage_instance, corpus) -> list:
    encoded_corpus = []
    for clause in corpus:
        encoded_clause = []
        for word in clause:
            word_indicator = storage_instance.put(word)
            encoded_clause.append(word_indicator)
        encoded_corpus.append(encoded_clause)
    return encoded_corpus


def split_by_sentence(text: str) -> list:
    if not isinstance(text, str) or text == '':
        return []

    if text[-1] not in ['.', '?', '!']:
        return []

    new_text = ''
    for index in range(len(text) - 1):

        if text[index] in ['.', '?', '!'] and text[index+1] is ' ':
            new_text += '.'

        if text[index].isalpha() or text[index] is ' ':
            new_text += text[index]

    new_text = new_text.split('.')
    sentence_list = []

    for sentence in new_text:
        sentence = '<s> ' + sentence.lower() + ' </s>'
        sentence_list.append(sentence.split())

    return sentence_list
