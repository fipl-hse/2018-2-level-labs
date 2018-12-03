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
        self.counter = 111

    def put(self, word):
        if not isinstance(word, str):
            return -1
        if word in self.storage:
            return -1
        self.storage[word] = self.counter
        self.counter += 1
        return self.storage[word]

    def get_id_of(self, word):
        if word in self.storage.keys():
            return self.storage[word]
        else:
            return -1

    def get_original_by(self, id):
        if id not in self.storage.values():
            return 'UNK'
        for word in self.storage.keys():
            if self.storage[word] == id:
                return word

    def from_corpus(self, corpus):
        if corpus and ' ' not in corpus:
            if corpus[0] != '<s>':
                for sentence in corpus:
                    for word in sentence:
                        WordStorage.put(self, word)
            else:
                for word in corpus:
                    WordStorage.put(self, word)
        else:
            return {}


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence):
        if not isinstance(sentence, tuple):
            return 'ERROR'
        grams_list = []
        if self.size == 2:
            for index in range(len(sentence) - 1):
                bi_gram = (sentence[index], sentence[index + 1])
                if bi_gram not in self.gram_frequencies.keys():
                    self.gram_frequencies[bi_gram] = 1
                else:
                    present_value = self.gram_frequencies[bi_gram]
                    self.gram_frequencies[bi_gram] = present_value + 1
        if self.size == 3:
            for index in range(len(sentence) - 2):
                three_gram = (sentence[index], sentence[index + 1], sentence[index + 2])
                if three_gram not in self.gram_frequencies.keys():
                    self.gram_frequencies[three_gram] = 1
                else:
                    present_value = self.gram_frequencies[three_gram]
                    self.gram_frequencies[three_gram] = present_value + 1
        for gram in grams_list:
            if gram in self.gram_frequencies:
                self.gram_frequencies[gram] += 1
            else:
                self.gram_frequencies[gram] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        if self.size == 2:
            for gram, freq in self.gram_frequencies.items():
                sum_of_freqs = 0
                for gram_2, freq_2 in self.gram_frequencies.items():
                    if gram[0] == gram_2[0]:
                        sum_of_freqs += freq_2
                    else:
                        continue
                gram_prob = math.log(freq / sum_of_freqs)
                self.gram_log_probabilities[gram] = gram_prob
        if self.size == 3:
            for gram, freq in self.gram_frequencies.items():
                sum_of_freqs = 0
                for gram_2, freq_2 in self.gram_frequencies.items():
                    if (gram[0] == gram_2[0]) and (gram[1] == gram_2[1]):
                        sum_of_freqs += freq_2
                    else:
                        continue
                gram_prob = math.log(freq / sum_of_freqs)
                self.gram_log_probabilities[gram] = gram_prob
        return 'OK'

    def predict_next_sentence(self, prefix):
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
                if len(probable_grams) == 0:
                    return predicted_sentence
                probable_grams.sort(reverse=True)
                predicted_sentence.append(probable_grams[0][1][1])
                word = probable_grams[0][1][1]
        if self.size == 3:
            predicted_sentence = [prefix[0], prefix[1], ]
            words = [prefix[0], prefix[1]]
            while True:
                probable_grams = []
                for gram, log_prob in self.gram_log_probabilities.items():
                    if gram[0] == words[0] and gram[1] == words[1]:
                        probable_grams.append((log_prob, gram))
                if len(probable_grams) == 0:
                    return predicted_sentence
                probable_grams.sort(reverse=True)
                predicted_sentence.append(probable_grams[0][1][2])
                words[0] = probable_grams[0][1][1]
                words[1] = probable_grams[0][1][2]


def encode(storage_instance, corpus):
    encoded = list()
    for sentence in corpus:
        lst = list()
        for word in sentence:
            lst.append(storage_instance.storage[word])
            encoded.append(lst)
    return encoded


def split_by_sentence(text: str):
    if not isinstance(text, str):
        return []
    if text == '':
        return []
    new_text = ''
    list_of_marks = [
        '.', ',', ':', '"', '`', '[', ']',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
    ]
    end_marks = ['.', '!', '?', '...', '\n']
    ready_words = []
    for sentence, element in enumerate(text):
        try:
            if (element in end_marks) and (text[sentence + 2].isupper()):
                try:
                    new_text += '.' + text[sentence + 1]
                    continue
                except IndexError:
                    pass
        except IndexError:
            pass
        if element in list_of_marks:
            continue
        new_text += element
    new_text = new_text.lower()
    sentences = new_text.split('. ')
    for sentence in sentences:
        splitted = sentence.split()
        splitted.insert(0, '<s>')
        splitted.append('</s>')
        ready_words.append(splitted)
    if (len(ready_words[0]) == 2) or (len(ready_words[0]) == 3):
        return []
    return ready_words
