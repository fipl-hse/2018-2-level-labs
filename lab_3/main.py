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
        self.storage = dict()
        self.counter = 0

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word in self.storage:
            return -1
        self.storage[word] = self.counter
        self.counter += 1
        return self.storage[word]

    def get_id_of(self, word:str) -> int:
        if word not in self.storage.keys():
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return 'UNK'
        for word in self.storage.keys():
            if self.storage[word] == id:
                return word

    def from_corpus(self, corpus: tuple) -> str:
        if not isinstance(corpus, tuple):
            return 'UNK'

        for word in corpus:
            if word in self.storage:
                continue
            self.storage[word] = self.counter
            self.counter += 1
        return 'OK'


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = dict()
        self.gram_log_probabilities = dict()

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'ERROR'
        list_of_grams = list()
        if self.size == 2:
            for index, code in enumerate(sentence):
                if len(sentence) == index + 1:
                    break
                list_of_grams.append((code, sentence[index + 1]))
        if self.size == 3:
            for index, code in enumerate(sentence):
                if len(sentence) == index + 2:
                    break
                list_of_grams.append((code, sentence[index + 1], sentence[index + 2]))

        for gram in list_of_grams:
            if gram in self.gram_frequencies:
                self.gram_frequencies[gram] += 1
            else:
                self.gram_frequencies[gram] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        if self.size == 2:
            for gram, freq in self.gram_frequencies.items():
                sum_of_freqs = 0 # gram from the same letter
                for gram_2, freq_2 in self.gram_frequencies.items():
                    if gram[0] == gram_2[0]:
                        sum_of_freqs += freq_2
                    else:
                        continue
                gram_prob = math.log(freq / sum_of_freqs)
                self.gram_log_probabilities[gram] = gram_prob
        if self.size == 3:
            for gram, freq in self.gram_frequencies.items():
                sum_of_freqs = 0 # gram from the same letter
                for gram_2, freq_2 in self.gram_frequencies.items():
                    if (gram[0] == gram_2[0]) and (gram[1] == gram_2[1]):
                        sum_of_freqs += freq_2
                    else:
                        continue
                gram_prob = math.log(freq / sum_of_freqs)
                self.gram_log_probabilities[gram] = gram_prob

        return 'OK'

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple):
            return []
        if len(prefix) != self.size - 1:
            return []
        sentence = list()
        if self.size == 2:
            word = prefix[0]
            sentence.append(word)
            while True:
                next_gram = list()
                for gram, gram_prob in self.gram_log_probabilities.items():
                    if gram[0] == word:
                        next_gram.append((gram_prob, gram))

                if len(next_gram) == 0:
                    return sentence

                next_gram.sort(reverse=True)
                sentence.append(next_gram[0][1][1])
                word = next_gram[0][1][1]

        if self.size == 3:
            words = [prefix[0], prefix[1]]
            sentence = [prefix[0], prefix[1], ]
            while True:
                next_gram = list()
                for gram, gram_prob in self.gram_log_probabilities.items():
                    if (gram[0] == words[0]) and (gram[1] == words[1]):
                        next_gram.append((gram_prob, gram))

                if len(next_gram) == 0:
                    return sentence

                next_gram.sort(reverse=True)
                sentence.append(next_gram[0][1][2])
                words[0] = next_gram[0][1][1]
                words[1] = next_gram[0][1][2]


def encode(storage_instance, corpus) -> list:
    encoded = list()
    for sentence in corpus:
        lst = list()
        for word in sentence:
            lst.append(storage_instance[word])
        encoded.append(lst)
    return encoded


def split_by_sentence(text):
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
    good_marks = ['.', '!', '?', '...', '\n']
    sentences = list()
    words = list()
    for sentence, element in enumerate(text):
        try:
            if (element in good_marks) and (text[sentence + 2].isupper()):
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
        words.append(splitted)
    if (len(words[0]) == 2) or (len(words[0]) == 3):
        return []
     
    return words
