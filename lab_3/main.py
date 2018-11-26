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
        self.size = 0
        self.storage = {}
        self.counter = 0

    def put(self, word: str) -> int:
        if type(word) != str:
            return self.storage
        if word in self.storage.keys():
            return self.storage[word]
        self.storage[word] = self.counter
        self.counter += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.storage.keys():
            self.storage[word] = -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if type(id) != int:
            return 'UNK'
        for key, value in self.storage.items():
            if id not in self.storage.values():
                return 'UNK'
            if value == id:
                return key

    def from_corpus(self, corpus: tuple):
        if type(corpus) != tuple or corpus == None:
            return self.storage
        for word in corpus:
            self.put(word)


class NGramTrie:
    def __init__(self, scale: int):
        self.size = scale
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        n_gram_list = []
        if type(sentence) is not tuple:
            return self.gram_frequencies
        for index, word in enumerate(sentence):
            if index == len(sentence) - 1:
                break
            n_gram_list.append((sentence[index], sentence[index + 1]))
        for couple in n_gram_list:
            if couple in self.gram_frequencies.keys():
                self.gram_frequencies[couple] += 1
            else:
                self.gram_frequencies[couple] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        for bi_gram, bi_gram_freq in self.gram_frequencies.items():
                word_n_1 = bi_gram[0]
                frequency = 0
                for bi_gram_second, bi_gram_freq_second in self.gram_frequencies.items():
                    if bi_gram_second[0] == word_n_1:
                        frequency += bi_gram_freq_second
                log_frequency = bi_gram_freq / frequency
                self.gram_log_probabilities[bi_gram] = math.log(log_frequency)
        return 'OK'

    def predict_next_sentence(self, prefix: tuple) -> list:
        storage_list = []
        for gram, frequency in self.gram_log_probabilities.items():
            if gram[0] == prefix[-1]:
                storage_list.append((gram, frequency))
            storage_list.sort(reverse=True)
            prefix = storage_list[0][1][1]

            while True:

            if storage_list == []:
                return predicted_sentence

        if len(prefix) != self.size - 1:
            return {}


def encode(storage_instance, corpus) -> list:
    encoding_sentence_list = []
    for sentence in corpus:
        encoding_words_list = []
        for word in sentence:
            if word in storage_instance.keys():
                word = storage_instance[word]
                encoding_words_list.append(word)
        encoding_sentence_list.append(encoding_words_list)
    return encoding_sentence_list


def split_by_sentence(text: str) -> list:
    new_text = ''
    words_list = []
    list_of_marks = [
        '.', ',', ':', '"', '`', '[', ']', '\n',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    sentence_endings = [
        '!', '?', '\n'
    ]
    for index, element in enumerate(text):
        if index == len(text) - 2:
            new_text += text[index:]
            break
        if element in sentence_endings and text[index + 2].isupper():
            new_text += '.'
            continue
        if element in list_of_marks:
            continue
        new_text += element
    sentences_list = new_text.split('. ')
    for sentence in sentences_list:
        sentence = sentence.lower()
        words = sentence.split()
        words_list.append(words)
        sentences_list.insert(0, "<s>")
        sentences_list.append("</s>")
    return words_list

