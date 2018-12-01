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
        self.id_counter = 0
     
    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word in self.storage:
            return -1
        self.storage[word] = self.id_counter
        self.id_counter += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.storage.keys():
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return None
        for word in self.storage.keys():
            if self.storage[word] == id:
                return word

    def from_corpus(self, corpus: tuple):
        if not isinstance(corpus, tuple):
            return {}
        for word in corpus:
            if word not in self.storage:
                self.storage[word] = self.counter
                self.counter += 1


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
    flag = 0
    if text == None:
        return []
    text = text.lower()
    for element in text:
        if element in alph:
            if flag == 0:
                new_text.append('<s>')
                flag = 1
            word += element

        if element != '.' and element != '!' and element != '?' and element != ' ':
            continue

        if word != '':
            new_text.append(word)
        
        if element != ' ':
            new_text.append('</s>')
            final_list.append(new_text)
            new_text = []
            flag = 0
                        
                        
        word = ''
    if word != '':        
        new_text.append(word)
return final_list
 
