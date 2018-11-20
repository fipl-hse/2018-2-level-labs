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
        return 1

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

    # Step 0. Test processing.
    if text is '' or text is None:
        return []
    if text[-1] not in ['.', '!', '?']:
        return []

    # Step 1. Making tokens.
    alphabet_checker = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_text = ''
    for element in text:
        if element in ['.', '!', '?']:
            new_text += '.'
        if element is ' ':
            new_text += ' '
        if element in alphabet_checker:
            new_text += element
    final = ''
    for index in range(len(new_text)-1):
        if new_text[index] is '.':
            if new_text[index+1] in alphabet_checker:
                continue
            if new_text[index+1] is '.':
                continue
        final += new_text[index]
    final = final.split('.')
    my_tokens = []
    for element in final:
        element = element.lower()
        element = '<s> ' + element + ' </s>'
        element = element.split()
        my_tokens.append(element)
    return my_tokens
