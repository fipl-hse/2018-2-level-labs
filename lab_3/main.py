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
    def put(self, word):
        pass

    def get_id_of(self, word):
        pass

    def get_original_by(self, id):
        pass

    def from_corpus(self, corpus):
        pass


class NGramTrie:
    def fill_from_sentence(self, sentence):
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix):
        pass


def encode(storage_instance, corpus):
    pass


def split_by_sentence(text):
    pass
