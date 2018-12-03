"""
Labour work #3
 Building an own N-gram model
"""

import math

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
        if el in alphabet_checker or el == ' ':
            n_text += el
        if el in punctuation:
            n_text += '.'
    result = ''
    for index in range(0, len(new_text) - 1):
        if new_text[index] is '.':
            if new_text[index + 1] in alphabet_checker or new_text[index + 1] is '.':
                continue
        result += new_text[index]
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
        self.store = {}

    def put(self, word: str) -> int:
        if word in self.store:
            return self.store[word]
        
        if not isinstance(word, str):
            return 0

        for value in self.store.values():
            if value == self.count:
                self.count += 1
                continue
        self.store[word] = self.count
        return self.count

    def get_id_of(self, word: str) -> int:
        if word is None or not isinstance(word, str) or word not in self.store:
            return -1
        else:
            return self.store[word]

    def get_original_by(self, num: int) -> str:
        if not isinstance(num, int):
            for key, value in self.store.items():
                if value == num:
                    return key
        return 'UNK'

    def from_corpus(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return ''
        for el in sentence:
            self.put(el)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.log_probability = {}
        self.frequency = {}

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
            if res in self.frequency:
                frequency_n = self.frequency[res]
                self.frequency[res] = frequency_n + 1
                continue
            self.frequency[tuple(res)] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        engram_list = []
        counter = 0

        for key in self.frequency:
            engram_list.append(key)
            continue

        while counter <= (len(engram_list) - 1):
            engrams_list = []
            sum_engram = 0
            engram_now = engram_list[counter]
            engram_now[:-1] = engram_now[:-1]
            for el in engram_list:
                if engram_now[:-1] == el[:-1]:
                    engrams_list.append(el)
                continue
            
            for el in engrams_list:
                sum_engram += self.frequency[el]
            logarithm = math.log(self.frequency[engram_list[counter]]/sum_engram)
            self.log_probability[engram_list[counter]] = logarithm
            counter += 1
            continue

    def predict_next_sentence(self, prefix: tuple) -> list:
        if self.log_probability == {}:
            return []
        prefix_list = list(prefix)
        length = len(prefix)
        counter = len(self.log_probability)
        while counter:
            engrams = []
            for key in self.log_probability.keys():
                if prefix_list[-length:] == list(key)[:length]:
                    engrams.append(key)

            logarithm = []
            for el in engrams:
                logarithm.append(self.log_probability[el])
            try:
                result = max(logarithm)
            except ValueError:
                break
            for key, value in self.log_probability.items():
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
