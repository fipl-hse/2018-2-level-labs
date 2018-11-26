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
        self.count = 0

    def put(self, word: str) -> int:
        if isinstance(word, str) is False or word in self.storage:
            return {}
        for element in self.storage.values():
            if element == self.count:
                self.count += 1
        self.storage[word] = self.count
        return self.count

    def get_id_of(self, word: str) -> int:
        if isinstance(word, str) is False or word not in self.storage:
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if isinstance(id, int) is False or id is None or id not in self.storage.values():
            return 'UNK'
        for word, number in self.storage.items():
            if number == id:
                return word

    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple) is False or corpus is None:
            return {}
        for word in corpus:
            self.put(word)


class NGramTrie:

    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if isinstance(sentence, tuple) is False or sentence is None:
            return 'ERROR'
        combinations = []
        for i in range(len(sentence) - 1):
            pair = [sentence[i], sentence[i + 1]]
            combinations.append(tuple(pair))
        for element in combinations:
            frequency = combinations.count(element)
            self.gram_frequencies[element] = frequency
        return 'OK'

    def calculate_log_probabilities(self):
        combinations = []
        for pair in self.gram_frequencies.keys():
            combinations.append(pair)
        for gram in combinations:
            frequency_sum = 0
            gram_frequency = self.gram_frequencies[gram]
            for another_gram in combinations:
                if another_gram[0] == gram[0]:
                    frequency_sum += self.gram_frequencies[another_gram]
            log_probability = math.log(gram_frequency / frequency_sum)
            self.gram_log_probabilities[gram] = log_probability

    def predict_next_sentence(self, prefix: tuple) -> list:
        if isinstance(prefix, tuple) is False or prefix is None or len(prefix) != self.size - 1:
            return []
        prefix = list(prefix)
        grams = []
        log_probabilities = []
        for key in self.gram_log_probabilities.keys():
            grams.append(key)
        for gram in grams:
            if prefix[-1] not in gram:
                continue
            if prefix[-1] == gram[0]:
                log_probabilities.append(self.gram_log_probabilities[gram])
            max_probability = max(log_probabilities)
            for key, value in self.gram_log_probabilities.items():
                if value == max_probability and key[-1] not in prefix:
                    prefix.append(key[-1])
                    log_probabilities = []
                    continue
        return prefix


def encode(storage_instance, corpus) -> list:
    sentence_id = []
    word_id = []
    for sentence in corpus:
        for word in sentence:
            word_id.append(storage_instance.put(word))
        sentence_id.append(word_id)
        word_id = []
        continue
    return sentence_id


def split_by_sentence(text: str) -> list:
    if text == '' or text is None or ' ' not in text:
        return []
    text = text.lower()
    text_accumulator = ''
    for element in text:
        if element in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' or element in ' .!?':
            text_accumulator += element
    words_list = text_accumulator.split(' ')
    sentence_list = ['<s>']
    text_list = []
    for word in words_list:
        if len(word) == 0:
            continue
        if word[-1] not in '.!?':
            sentence_list.append(word)
        else:
            word = word.replace(word[-1], '')
            sentence_list.append(word)
            sentence_list.append('</s>')
            text_list.append(sentence_list)
            sentence_list = ['<s>']
            continue
    return text_list
