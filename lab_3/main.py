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
 #       self.counter = 0

    def put(self, word: str) -> int:
        pass
        id = 0
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
 #           return self.storage[word]

    def get_id_of(self, word: str) -> int:
        pass
        if word in self.storage.keys():
            return self.storage[word]
        else:
            return -1

    def get_original_by(self, id_word: int) -> str:
        pass
        if not isinstance(id_word, int):
            return 'UNK'
        for word, value in self.storage.items():
            if value == id_word:
                return word
        return 'UNK'

    def from_corpus(self, corpus: tuple) -> str:
        pass
        if not isinstance(corpus, tuple):
            return ''
        for sentence in corpus:
            self.put(sentence)



class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        pass
        if not isinstance(sentence, tuple):
            return 'ERROR'

        if sentence and isinstance(sentence, tuple):
            if self.size == 2:
                for i in range(len(sentence) - 1):
                    two_gram = (sentence[i], sentence[i + 1])
                    if two_gram not in self.gram_frequencies.keys():
                        self.gram_frequencies[two_gram] = 1
                    else:
                        value = self.gram_frequencies[two_gram]
                        self.gram_frequencies[two_gram] = value + 1
            elif self.size == 3:
                for i in range(len(sentence) - 2):
                    three_gram = (sentence[i], sentence[i + 1], sentence[i + 2])
                    if three_gram not in self.gram_frequencies.keys():
                        self.gram_frequencies[three_gram] = 1
                    else:
                        value = self.gram_frequencies[three_gram]
                        self.gram_frequencies[three_gram] = value + 1
        return 'OK'


    def calculate_log_probabilities(self):
        pass
        if self.size == 2:
            for key, value in self.gram_frequencies.items():
                probability = 0
                for two_key, two_value in self.gram_frequencies.items():
                    if key[0] == two_key[0]:
                        probability += two_value
                    else:
                        continue
                gram_probability = value / probability
                gram_log_probability = math.log(gram_probability)
                self.gram_log_probabilities[key] = gram_log_probability
        elif self.size == 3:
            for key, value in self.gram_frequencies.items():
                probability = 0
                for two_key, two_value in self.gram_frequencies.items():
                    if key[0] == two_key[0] and key[1] == two_key[1]:
                        probability += two_value
                    else:
                        continue
                gram_probability = value / probability
                gram_log_probability = math.log(gram_probability)
                self.gram_log_probabilities[key] = gram_log_probability
        return 'OK'


    def predict_next_sentence(self, prefix: tuple) -> list:
        pass
        if not isinstance(prefix, tuple) or not prefix:
            return []
        if len(prefix) != self.size - 1:
            return []
        if self.size == 2:
            sentence = [prefix[0], ]
            word = prefix[0]
            while True:
                expected_res = []
                for key, value in self.gram_log_probabilities.items():
                    if key[0] == word:
                        expected_res.append((value, key))
                if len(expected_res) == 0:
                    return sentence
                expected_res.sort(reverse = True)
                sentence.append(expected_res[0][1][1])
                word = expected_res[0][1][1]
        elif self.size == 3:
            sentence = [prefix[0], prefix[1], ]
            word = [prefix[0], prefix[1]]
            while True:
                expected_res = []
                for key, value in self.gram_log_probabilities.items():
                    if key[0] == word[0] and key[1] == word[1]:
                        expected_res.append((value, key))
                if len(expected_res) == 0:
                    return sentence
                expected_res.sort(reverse=True)
                sentence.append(expected_res[0][1][2])
                word[0] = expected_res[0][1][1]
                word[1] = expected_res[0][1][2]
                
