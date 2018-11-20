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
        if word is None or not isinstance(word, str) or word not in self.storage:
            return -1
        return self.storage[word]

    def get_original_by(self, number: int) -> str:
        if not isinstance(number, int):
            return 'UNK'
        for key, value in self.storage.items():
            if value == number:
                return key
        return 'UNK'

    def from_corpus(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return ''
        for element in sentence:
            self.put(element)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'ERROR'

        # N Grams.
        list_of_n_grams = []
        for element in range(0, (len(sentence)-1)):
            list_of_n_grams.append(sentence[element:element+self.size])
        res = []
        for n_gram in list_of_n_grams:
            if len(n_gram) == self.size:
                res.append(n_gram)
        for n_gram in res:
            frequency = list_of_n_grams.count(n_gram)
            self.gram_frequencies[tuple(n_gram)] = frequency
        return 'OK'

    def calculate_log_probabilities(self):
        list_of_engrams = []
        for key in self.gram_frequencies:  # .keys()
            list_of_engrams.append(key)
            continue

        # N Grams.
        counter = 0
        while counter <= (len(list_of_engrams)-1):
            engrams_list = []
            current_engram = list_of_engrams[counter]
            w_engram = current_engram[:-1]
            for engram in list_of_engrams:
                if w_engram == engram[:-1]:
                    engrams_list.append(engram)
                continue
            engrams_list_sum = 0
            for engram in engrams_list:
                engrams_list_sum += self.gram_frequencies[engram]
            log = math.log(self.gram_frequencies[list_of_engrams[counter]] / engrams_list_sum)
            self.gram_log_probabilities[list_of_engrams[counter]] = log
            counter += 1
            continue

    def predict_next_sentence(self, prefix: tuple) -> list:

        # Step 0. Test Processing.
        if self.gram_log_probabilities == {}:
            return []

        # N Grams.
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

    # Step 0. Test processing.
    space = ' '
    non_space = ''
    if text is non_space or text is None:
        return []
    if text[-1] not in ['.', '!', '?']:
        return []

    # Step 1. Making tokens.
    alphabet_checker = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_text = ''
    for element in text:
        if element in ['.', '!', '?']:
            new_text += '.'
        if element is space:
            new_text += ' '
        if element in alphabet_checker:
            new_text += element
    final = ''
    for index in range(0, len(new_text)-1):
        dot = '.'
        if new_text[index] is dot:
            if new_text[index+1] in alphabet_checker:
                continue
            if new_text[index+1] is dot:
                continue
        final += new_text[index]
    final = final.split('.')
    my_tokens = []
    for element in final:
        element = element.lower()
        element = '<s> ' + element + ' </s>'
        element = element.split()
        my_tokens.append(element)
    return my_tokens
