"""
Labour work #3
 Building an own N-gram model
"""
from math import log

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


def read_from_file(path_to_file, lines_limit: int) -> str:
    my_text = ''
    lines_count = 0
    my_file = open(path_to_file, 'r')
    for line in my_file:
        if lines_count == lines_limit:
            return my_text
        my_text += line
        lines_count += 1
    my_file.close()
    return my_text


def split_by_sentence(text: str) -> list:
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
    marks_well = ['.', '!', '...', '?', '\n']
    list_of_results = list()

    for index, element in enumerate(text):
        try:
            if element in marks_well and text[index + 2].isupper():
                try:
                    new_text += '.'
                    continue
                except IndexError:
                    pass
        except IndexError:
            pass
        if element in list_of_marks:
            continue
        new_text += element
    sentences_list = new_text.split('. ')

    for sentence in sentences_list:
        sentence = sentence.lower()
        splitter = sentence.split()
        splitter.insert(0, '<s>')
        splitter.append('</s>')
        list_of_results.append(splitter)

    if len(list_of_results[0]) == 2 or len(list_of_results[0]) == 3:
        return []

    return list_of_results


class WordStorage:
    def __init__(self):
        self.counter = 0
        self.storage = dict()

    def put(self, word: str) -> int:
        if not isinstance(word, str) or word in self.storage.keys():
            return -1

        self.storage[word] = self.counter
        self.counter += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.storage:
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return 'UNK'

        for word, word_id in self.storage.items():
            if word_id == id:
                return word

    def from_corpus(self, corpus: tuple) -> str:
        if not isinstance(corpus, tuple):
            return 'Error'

        for word in corpus:
            self.put(word)
        return 'OK'


def encode(storage_instance, corpus: tuple) -> list:
    if not isinstance(corpus, tuple):
        return []

    encoded_list = list()
    for sentence in corpus:
        inner_list = list()
        for word in sentence:
            inner_list.append(storage_instance.storage[word])
        encoded_list.append(inner_list)
    return encoded_list


class NGramTrie:
    def __init__(self, scale: int):
        self.size = scale
        self.gram_frequencies = dict()
        self.gram_log_probabilities = dict()

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'Error'

        grams_list = list()

        for index in range(0, (len(sentence) - 1)):
            if index == len(sentence) - (self.size - 1):
                break
            gram = (sentence[index: index + self.size])
            grams_list.append(gram)

        for gram in grams_list:
            self.gram_frequencies[gram] = self.gram_frequencies.get(gram, 0) + 1

        return 'OK'

    def calculate_log_probabilities(self):
        if self.size == 2:
            for gram, freq in self.gram_frequencies.items():
                general_probability = 0
                for gram_2, freq_2 in self.gram_frequencies.items():
                    if gram[0] == gram_2[0]:
                        general_probability += freq_2
                    else:
                        continue

                gram_probability = freq / general_probability
                gram_log_probability = log(gram_probability)
                self.gram_log_probabilities[gram] = gram_log_probability

        elif self.size == 3:
            for gram, freq in self.gram_frequencies.items():
                general_probability = 0
                for gram_2, freq_2 in self.gram_frequencies.items():
                    if (gram[0] == gram_2[0]) and gram[1] == gram_2[1]:
                        general_probability += freq_2
                    else:
                        continue

                gram_probability = freq / general_probability
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

                if len(probable_grams) == 0:
                    return predicted_sentence

                probable_grams.sort(reverse=True)
                predicted_sentence.append(probable_grams[0][1][1])
                word = probable_grams[0][1][1]

        elif self.size == 3:
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

