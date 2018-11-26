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

    def put(self, word: str) -> int:
        if word is None or not isinstance(word, str):
            return {}
        new_count = 1
        if word not in self.storage.keys():
            if self.storage:
                new_count = max(self.storage.keys()) + 1
                self.storage[word] = new_count
            else:
                self.storage[word] = new_count
        return new_count

    def get_id_of(self, word: str) -> int:
        if word not in self.storage or word is None or  not isinstance(word, str):
            return -1
        else:
            return self.storage[word]


    def get_original_by(self, id: int) -> str:
        if id is None or not isinstance(id, int):
            return('UNK')

        if id in self.storage.values():
            for word, value in self.storage.items():
                if value == id:
                    return word
        else:
            return ('UNK')


    def from_corpus(self, corpus: tuple):
        if corpus == () or corpus is None or not isinstance(corpus, tuple):
            return {}
        if corpus:
            for word in corpus:
                WordStorage.put(self, word)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if isinstance(sentence, tuple):
            if self.size == 2:
                for index in range(len(sentence) - 1):
                    bi_gram = (sentence[index], sentence[index + 1])
                    if bi_gram not in self.gram_frequencies.keys():
                        self.gram_frequencies[bi_gram] = 1
                    else:
                        new_count = self.gram_frequencies[bi_gram]
                        self.gram_frequencies[bi_gram] += 1
                return 'OK'
        else:
            return 'ERROR'


    def calculate_log_probabilities(self):
        for n_gram in self.gram_frequencies:
            count = 0
            n_gram_parted = n_gram[:-1]
            for index, number in enumerate(list(self.gram_frequencies.keys())):
                if n_gram_part == number[:-1]:
                    count += list(self.gram_frequencies.values())[index]
            probability = self.gram_frequencies[n_gram] / count
            self.gram_log_probabilities[n_gram] = math.log(probability)
        return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:
        if prefix is None or prefix is ' ' or not isinstance(prefix, tuple):
            return []
        if self.gram_log_probabilities == {}:
            return []
        prefix_list = list(prefix)
        length = len(prefix)
        count = len(self.gram_log_probabilities)
        while count:
            engrams_list = []
            for key, value in self.gram_log_probabilities.items():
                current_key = list(key)
                if prefix_list[-length:] == current_key[:length]:
                    engrams_list.append(key)
            list_log = []
            for engram in engrams_list:
                list_log.append(self.gram_log_probabilities[engram])
            try:
                res = max(list_log)
            except ValueError:
                break
            for key, value in self.gram_log_probabilities.items():
                if res == value:
                    prefix_list.append(key[-1])
            count -= 1
        return prefix_list




def encode(storage_instance, corpus) -> list:
    new_sentense_corpus = []
    for sentence in corpus:
        for word in sentence:
            number = storage_instance.put(word)
            sentence_id.append(number)
            new_sentense_corpus.append(sentence_id)
            sentence_id = []
            continue

    return corpus_n




def split_by_sentence(text: str) -> list:
    word_in_sentence_list = []
    if text  and isinstance(text, str) and ' ' in text:


        text = text.lower()
        list_of_marks = [
            ',', ':', '"', '`', '[', ']',
            '?', '!', '@', '&', "'", '-',
            '$', '^', '*', '(', ')',
            '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                                                            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result = ''
        new_text = ''
        signs = ['.', '!', '?']
        for sign in text:
            if sign in signs:
                new_text += '.'
            if sign is ' ':
                new_text += ' '
            if sign in alphabet:
                new_text += sign

        for index in range(0, len(new_text) - 1):
            if new_text[index] is '.':
                if new_text[index + 1] in alphabet:
                    continue

            result += new_text[index]
        result = result.split('.')
        word_in_sentence_list = []
        for sentence in result:
            sentence = '<s> ' + sentence + ' </s>'
            sentence = sentence.split()
            word_in_sentence_list.append(sentence)
    return(word_in_sentence_list)
