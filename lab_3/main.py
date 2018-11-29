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
        ngram_list = []
        if not isinstance(sentence, tuple):
            return 'ERROR'
        for i, word in enumerate(sentence):
            if self.size == 2:
                if i == len(sentence) - 1:
                    break
                ngram_list.append((sentence[i], sentence[i + 1]))
            if self.size == 3:
                if i == len(sentence) - 2:
                    break
                ngram_list.append((sentence[i], sentence[i + 1], sentence[i + 2]))
        for both in ngram_list:
            if both in self.gram_frequencies.keys():
                self.gram_frequencies[both] += 1
            else:
                self.gram_frequencies[both] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        for bigram, bigram_freq in self.gram_frequencies.items():
            word_n_1 = bigram[0]
            frequency = 0
            for bigram_second, bigram_freq_second in self.gram_frequencies.items():
                if self.size == 2:
                    if bigram_second[0] == word_n_1:
                        frequency += bigram_freq_second
                if self.size == 3:
                    if bigram_second[0] == bigram[0] and bigram_second[1] == bigram[1]:
                        frequency += bigram_freq_second
            log_frequency = bigram_freq / frequency
            self.gram_log_probabilities[bigram] = math.log(log_frequency)
        return 'OK'

    def predict_next_sentence(self, prefix: tuple) -> list:
        predict_sentence = []
        if type(prefix) is not tuple:
            return []
        if len(prefix) != self.size - 1:
            return []
        if self.size == 2:
            word = prefix[0]
            predict_sentence.append(word)
            while True:
                storagelist = []
                for gram, frequency in self.gram_log_probabilities.items():
                    if gram[0] == word:
                        storagelist.append((frequency, gram))
                if len(storagelist) == 0:
                    return predict_sentence
                storagelist.sort(reverse=True)
                word = storagelist[0][1][1]
                predict_sentence.append(word)
        if self.size == 3:
            words = [prefix[0], prefix[1]]
            predict_sentence.append(words[0])
            predict_sentence.append(words[1])
            while True:
                storagelist = []
                for gram, frequency in self.gram_log_probabilities.items():
                    if gram[0] == words[0] and gram[1] == words[1]:
                        storagelist.append((frequency, gram))
                if len(storagelist) == 0:
                    return predict_sentence
                storagelist.sort(reverse=True)
                word = storagelist[0][1][2]
                predict_sentence.append(word)
                words[0] = storagelist[0][1][1]
                words[1] = word
        pass


def encode(storage_instance, corpus) -> list:
    encode = []
    for sentence in corpus:
        for key,value in storage_instance.items():
            if key in sentence:
                encode.append(storage_instance[key])
    return encode
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