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
    def put(self, word: str) -> int:
        pass

    def get_id_of(self, word: str) -> int:
        pass

    def get_original_by(self, id: int) -> str:
        pass

    def from_corpus(self, corpus: tuple):
        pass


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
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = []
    final_list = []
    word = ''
    text = text.lower()
    flag = 0
    for element in text:
        if element in alph:
            if flag == 0:
                new_text.append('<s>')
                flag = 1
            word += element

        else:
            if word != '':
                new_text.append(word)
            word = ''
            if element == '.' or element == '!' or element == '?':
                new_text.append('</s>')
                final_list.append(new_text)
                new_text = []
                flag = 0
    if word != '':        
        new_text.append(word)
    return final_list
 
