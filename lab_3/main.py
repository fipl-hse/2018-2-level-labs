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
        self.count = 1

    def put(self, word: str) -> int:
        if word != str(word) or word in self.storage:
            return self.storage
        for value in self.storage.values():
            if value == self.count:
                self.count += 1
        self.storage[word] = self.count
        return self.count

    def get_id_of(self, word: str) -> int:
        if word != str(word) or word not in self.storage.keys():
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return 'UNK'
        for key, value in self.storage.items():
            if value == id:
                return key

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
        if sentence is None or sentence != tuple(sentence) or sentence == ():
            return 'ERROR'
        combinations = []
        start = 0
        while start != len(sentence)-1:
            double = [sentence[start], sentence[start+1]]
            prefix = tuple(double)
            combinations.append(prefix)
            start += 1
        for element in combinations:
            freq = combinations.count(element)
            self.gram_frequencies[element] = freq
        return 'OK'

    def calculate_log_probabilities(self):
        pairs = []
        for key in self.gram_frequencies.keys():
            pairs.append(key)
        count = 0
        while count != len(pairs):
            for gram in pairs:
                all_gram = []
                gram_count = self.gram_frequencies[gram]
                for extra_gram in pairs:
                    if gram[0] == extra_gram[0]:
                        all_gram.append(self.gram_frequencies[extra_gram])
                count_all_gram = sum(all_gram)
                e_log = math.log(gram_count / count_all_gram)
                self.gram_log_probabilities[gram] = e_log
                count += 1

    def predict_next_sentence(self, prefix: tuple) -> list:
        if self.gram_log_probabilities is None or self.gram_log_probabilities == {}:
            return []
        prefix = list(prefix)
        count = 0
        values = []
        pairs = []
        for key in self.gram_log_probabilities.keys():
            pairs.append(key)
        while count != len(pairs):
            for n_gram in pairs:
                if n_gram[0] == prefix[-1]:
                    values.append(self.gram_log_probabilities[n_gram])
            if values == []:
                return prefix
            max_val = max(values)
            for key, value in self.gram_log_probabilities.items():
                if value == max_val:
                    prefix.append(key[-1])
            values = []
            count += 1
        return prefix


def encode(storage_instance, corpus) -> list:
    pass


def split_by_sentence(text: str) -> list:
    list_of_marks = [
        ',', ':', '"', '`', '[', ']', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
    ]
    if text == '' or text is None:
        return []
    new_text = ''
    for element in text:
        if element not in list_of_marks:
            new_text += element
    points = ['!', '?']
    for element in new_text:
        if element in points:
            new_text = new_text.replace(element, '.')
    new_text = new_text.lower()
    splitted_text = new_text.split('.')
    splitted_text.remove(splitted_text[-1])
    if splitted_text == ['']:
        return []
    final = []
    for sentence in splitted_text:
        new_list = ['<s>']
        list_sent = sentence.split(' ')
        for element in list_sent:
            if element is not '':
                new_list.append(element)
        new_list.append('</s>')
        final.append(new_list)
    return final


