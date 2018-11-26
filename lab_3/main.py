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
    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    pass


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
