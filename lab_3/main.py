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

    def put(self, word:str) -> int:
        id = 1
        if word and isinstance(word, str):
            if word not in self.storage.keys():
                if self.storage:
                    id = max(self.storage.values()) + 1
                    self.storage[word] = id
                else:
                    self.storage[word] = id
            return self.storage[word]
        else:
            return self.storage

    def get_id_of(self, word: str) -> int:
        if word in self.storage.keys():
            return self.storage[word]
        else:
            return -1

    def get_original_by(self, id: int) -> str:
        if id in self.storage.values():
            for word in self.storage.keys():
                if id == self.storage[word]:
                    return word
        else:
            return 'UNK'

    def from_corpus(self, corpus: tuple):
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

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence and isinstance(sentence, tuple):
            for index in range(len(sentence) - 1):
                bi_gram = (sentence[index], sentence[index + 1])
                if bi_gram not in self.gram_frequencies.keys():
                    self.gram_frequencies[bi_gram] = 1
                else:
                    present_value = self.gram_frequencies[bi_gram]
                    self.gram_frequencies[bi_gram] = present_value + 1
            return 'OK'
        else:
            return 'ERROR'

    def calculate_log_probabilities(self):
        import math
        for bi_gram in self.gram_frequencies.keys():
            w = bi_gram[1]
            denominator = 0
            for bi_gram in self.gram_frequencies.keys():
                if bi_gram[1] == w:
                    denominator += 1
            numerator = self.gram_frequencies[bi_gram]
            log_probability = math.log(numerator / denominator)
            self.gram_log_probabilities[bi_gram] = log_probability

    def get_bi_gram_by_probability(self, probability: int, dictionary: dict) -> tuple:
        if probability in dictionary.values():
            for bi_gram in dictionary.keys():
                if probability == dictionary[bi_gram]:
                    return bi_gram
        else:
            return 'UNK'

    def helper_for_prediction(self, prefix: tuple) -> tuple: #ищет максимальную вероятность из би-граммов вида (<число из префикса>, <что найдется в словаре>)
        current_dict = {}
        for bi_gram in self.gram_log_probabilities.keys():
            if bi_gram[0] == prefix[0]:
                current_dict[bi_gram] = self.gram_log_probabilities[bi_gram]
        probability_of_most_probable_bi_gram = max(current_dict.values())
        result = NGramTrie.get_bi_gram_by_probability(self, probability_of_most_probable_bi_gram, current_dict)
        return result

    def predict_next_sentence(self, prefix: tuple) -> list:
        import re
        result = []
        if prefix and isinstance(prefix, tuple):
            if len(prefix) == 1:
                result += prefix
                str_of_bi_grams = ''
                for bi_gram in self.gram_log_probabilities.keys():
                    str_of_bi_grams += str(bi_gram)
                    str_of_bi_grams += ' '
                while re.search(str(prefix), str_of_bi_grams):
                    next_word = NGramTrie.helper_for_prediction(self, prefix)
                    result.append(next_word[1])
                    prefix = (next_word[1],)
        return result
