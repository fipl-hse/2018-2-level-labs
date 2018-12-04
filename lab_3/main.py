"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


def split_by_sentence(text: str) -> list:
    punctuation = ['.', '!', '?']
    if text is '' or text is None:
        return []

    if text[-1] not in punctuation or text[-1].isalpha():
        return []

    n_text = ''
    for el in text:
        if el.isalpha() or el == ' ':
            n_text += el
        if el in punctuation:
            n_text += '.'
    result = ''
    for index in range(0, len(n_text) - 1):
        if n_text[index] == '.':
            if n_text[index + 1].isalpha() or n_text[index + 1] == '.':
                continue
        result += n_text[index]
    result = result.split('.')
    token = []
    for el in result:
        el = el.lower()
        el = '<s> ' + el + ' </s>'
        el = el.split()
        token.append(el)
    return token


class WordStorage:
    def __init__(self):
        self.count = 100000
        self.storage = {}

    def put(self, word: str) -> int:
        if word in self.storage:
            return self.storage[word]
        
        if not isinstance(word, str):
            return 0

        for value in self.storage.values():
            if value == self.count:
                self.count += 1
                continue
        self.storage[word] = self.count
        return self.count

    def get_id_of(self, word: str) -> int:
        if word is None or not isinstance(word, str) or word not in self.storage:
            return -1
        else:
            return self.storage[word]

    def get_original_by(self, num: int) -> str:
        if not isinstance(num, int) or num < 100000:
            return 'UNK'
        for key, value in self.storage.items():
                if value == num:
                    return key

    def from_corpus(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return ''
        for el in sentence:
            self.put(el)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_log_probabilities = {}
        self.gram_frequencies = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'ERROR'

        n_gram_list = []
        result = []

        for el in range(0, (len(sentence) - 1)):
            n_gram_list.append(sentence[el:el + self.size])
        for element in n_gram_list:
            if len(element) == self.size:
                result.append(element)
        for res in result:
            if res in self.gram_frequencies:
                frequency_n = self.gram_frequencies[res]
                self.gram_frequencies[res] = frequency_n + 1
                continue
            self.gram_frequencies[tuple(res)] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        engram_list = []
        counter = 0

        for key in self.gram_frequencies:
            engram_list.append(key)
            continue

        while counter <= (len(engram_list) - 1):
            engrams_list = []
            sum_engram = 0
            engram_now = engram_list[counter]
            for el in engram_list:
                if engram_now[:-1] == el[:-1]:
                    engrams_list.append(el)
                continue
            
            for el in engrams_list:
                sum_engram += self.gram_frequencies[el]
            logarithm = math.log(self.gram_frequencies[engram_list[counter]]/sum_engram)
            self.gram_log_probabilities[engram_list[counter]] = logarithm
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
            for key in self.gram_log_probabilities.keys():
                if prefix_list[-length:] == list(key)[:length]:
                    engrams.append(key)

            logarithm = []
            for el in engrams:
                logarithm.append(self.gram_log_probabilities[el])
            try:
                result = max(logarithm)
            except ValueError:
                break
            for key, value in self.gram_log_probabilities.items():
                    if result == value:
                        if key in engrams:
                            prefix_list.append(key[-1])
                            break
            counter -= 1
        return prefix_list


def encode(storage_instance, corpus) -> list:
    n_corpus = []
    sentence_id = []
    for sentence in corpus:
        for word in sentence:
            num = storage_instance.put(word)
            sentence_id.append(num)
        n_corpus.append(sentence_id)
        sentence_id = []
        continue
    return n_corpus
