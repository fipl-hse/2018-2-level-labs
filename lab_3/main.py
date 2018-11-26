"""
Labour work #3
 Building an own N-gram model
"""

import math

import random


REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.id = 0
        self.storage = {}

    def put(self, word: str) -> int:
        if word is None:
            return None
        if not isinstance(word,str):
            return {}
        else:
            if word in self.storage:
                return self.storage[word]
            else:
                id = random.randint(1, 300000)
                while id in self.storage.values():
                    id = random.randint(1, 300000)
                self.storage[word] = id
                return self.storage[word]


        pass

    def get_id_of(self, word: str) -> int:
        if word == None or type(word)!= str or word not in self.storage:
            return -1
        else:
            return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if type(id) != int:
            return 'UNK'
        for key, value in self.storage.items():
            if value == id:
                return key
        return 'UNK'
        pass

    def from_corpus(self, corpus: tuple):
        if corpus is None or type(corpus)!= tuple:
            return ''
        for word in corpus:
            self.put(word)
        pass


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence and type(sentence) == tuple:
            if self.size == 2:
                for index in range(len(sentence) - 1):
                    gramm_2 = (sentence[index], sentence[index + 1])
                    if gramm_2 not in self.gram_frequencies.keys():
                        self.gram_frequencies[gramm_2] = 1
                    else:
                        new_value = self.gram_frequencies[gramm_2]
                        self.gram_frequencies[gramm_2] = new_value + 1
            elif self.size == 3:
                for index in range(len(sentence) - 2):
                    gramm_3 = (sentence[index], sentence[index + 1], sentence[index + 2])
                    if gramm_3 not in self.gram_frequencies.keys():
                        self.gram_frequencies[gramm_3] = 1
                    else:
                        new_value = self.gram_frequencies[gramm_3]
                        self.gram_frequencies[gramm_3] = new_value + 1
            return 'OK'
        else:
            return 'ERROR'
        pass

    def calculate_log_probabilities(self):
        if self.size == 2:
            for gram, frequency in self.gram_frequencies.keys():
                general_probability = 0
                for gram_2, frequency_2 in self.gram_frequencies.keys():
                    if gram[0] == gram_2[0]:
                        general_probability += frequency_2
                    else:
                        continue
                gram_probability = frequency / general_probability
                gram_log_probability = log(gram_probability)
                self.gram_log_probabilities[gram] = gram_log_probability
        elif self.size == 3:
            for gram, frequency in self.gram_frequencies.keys():
                general_probability = 0
                for gram_2, frequency_2 in self.gram_frequencies.keys():
                    if (gram[0] == gram_2[0]) and gram[1] == gram_2[1]:
                        general_probability += frequency_2
                    else:
                        continue
                gram_probability = frequency / general_probability
                gram_log_probability = log(gram_probability)
                self.gram_log_probabilities[gram] = gram_log_probability
        return 'OK'

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or len(prefix) != self.size - 1:
            return []
        if self.size == 2:
            predicted_sentence = [prefix[0], ]
            word = prefix[0]
            while True:
                probable_grams = []
                for gram, log_prob in self.gram_log_probabilities.items():
                    if gram[0] == word:
                        probable_grams.append((log_prob, gram))
        pass


def encode(storage_instance, corpus) -> list:
    corp_1 = []
    id_sent = []
    for sentence in corpus:
        for word in sentence:
            number = storage_instance.get(word)
            id_sent.append(number)
        corp_1.append(id_sent)
        id_sent = []
        continue
    return corp_1
    pass


def split_by_sentence(text: str) -> list:

    if text is None or text == '':
        return []
    if text[-1] not in ['.', '!', '?']:
        return []

    text_new = ''
    for word in text:
        if word in ['.', '!', '?']:
            text_new += '.'
        if word == ' ':
            text_new += ' '
        if word.isalpha():
            text_new += word
    final = ''
    for current in range(0, len(text_new) - 1):
        if text_new[current] == '.':
            if text_new[current + 1].isalpha():
                continue
            if text_new[current + 1] == '.':
                continue
        final += text_new[current]
    final = final.split('.')
    tokens = []
    for word in final:
        word = word.lower()
        word = '<s> ' + word + ' </s>'
        word = word.split()
        tokens.append(word)
    return tokens