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
    if text == '' or text is None:
        return []
    text = 'Mar#y wa$nted, to swim! However, she was afraid of sharks.'
    list_of_marks = [
        ',', ':', '"', '`', '[', ']', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
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


