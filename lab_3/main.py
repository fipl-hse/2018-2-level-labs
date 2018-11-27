"""
Labour work #3
 Building an own N-gram model
"""

import math


REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()

class WordStorage:
    def __init__(self):
        self.storage = {}

        self.counter = 0
    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return 0
        if word in self.storage:
            return self.storage[word]
        for value in self.storage.values():
            if value == self.counter:
                self.counter += 1
                continue
        self.storage[word] = self.counter
        return self.counter


    def get_id_of(self, word: str) -> int:
        if word != str(word) or word not in self.storage.keys():
            return -1
        return self.storage[word]


    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return 'UNK'

        for word, word_id in self.storage.items():
            if word_id == id:
                return word


    def from_corpus(self, corpus: tuple):
        if corpus is None or corpus != tuple(corpus):
            return {}
        for word in corpus:
            self.put(word)



class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'Error'
        list_of_ngrams = []
        for i in range(0, (len(sentence) - 1)):
            list_of_ngrams.append(sentence[i: i + self.size])
        res = []
        for n_gram in list_of_ngrams:
            if len(n_gram) == self.size:
                res.append(n_gram)
        for n_gram in res:
            frequency = list_of_ngrams.count(n_gram)
            self.gram_frequencies[tuple(n_gram)] = frequency
        return 'OK'

    def calculate_log_probabilities(self):
        engram_list = []
        for key in self.gram_frequencies:
            engram_list.append(key)
            continue
        counter = 0
        while counter <= (len(engram_list) - 1):
            list_of_engrams = []
            current_engram = engram_list[counter]
            w_engram = current_engram[:-1]
            for engram in engram_list:
                if w_engram == engram[:-1]:
                    list_of_engrams.append(engram)
                continue
            engrams_sum = 0
            for engram in list_of_engrams:
                engrams_sum += self.gram_frequencies[engram]
            log = math.log(self.gram_frequencies[engram_list[counter]] / engrams_sum)
            self.gram_log_probabilities[engram_list[counter]] = log
            counter += 1
            continue


    def predict_next_sentence(self, prefix: tuple) -> list:
        if self.gram_log_probabilities == {}:
            return []
        prefix_list = list(prefix)
        length = len(prefix)
        counter = len(self.gram_log_probabilities)
        while counter:
            engrams = []
            for key, value in self.gram_log_probabilities.items():
                current_key = list(key)
                if prefix_list[-length:] == current_key[:length]:
                    engrams.append(key)
            logs = []

            for engram in engrams:
                logs.append(self.gram_log_probabilities[engram])
            try:
                res = max(logs)
            except ValueError:
                break

            for key, value in self.gram_log_probabilities.items():
                if res == value:
                    prefix_list.append(key[-1])
            counter -= 1
        return prefix_list

    def encode(storage_instance, corpus) -> list:
        new_corpus = []
        id_sentence = []
        for sentence in corpus:
            for word in sentence:
                number = storage_instance.put(word)
                id_sentence.append(number)
            new_corpus.append(id_sentence)
            id_sentence = []
            continue
        return new_corpus
    def split_by_sentence(text: str) -> list:
        with_space = ' '
        no_space = ''
        if text is no_space or text is None:
            return []
        if text[-1] not in ['.', '!', '?']:
            return []
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                                                       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        new_text = ''
        for el in text:
            if el in ['.', '!', '?']:
                new_text += '.'
            if el is with_space:
                new_text += ' '
            if el in abc:
                new_text += el
        final = ''
        for index in range(0, len(new_text) - 1):
            point = '.'
            if new_text[index] is point:
                if new_text[index + 1] in abc:
                    continue
                if new_text[index + 1] is point:
                    continue
            final += new_text[index]
        final = final.split('.')
        tokens = []
        for element in final:
            element = element.lower()
            element = '<s> ' + element + ' </s>'
            element = element.split()
            tokens.append(element)
        return tokens



