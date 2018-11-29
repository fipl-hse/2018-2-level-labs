"""
Labour work #3
 Building an own N-gram model
"""

import math

#REFERENCE_TEXT = ''
#if __name__ == '__main__':
    #with open('not_so_big_reference_text.txt', 'r') as f:
        #REFERENCE_TEXT = f.read()

text = """Ma3ry # wan$ted to swim! Ho*&wever, sh5e w#as afra<id of shar>ks."""
punct_marks = ['.', '!', '?']
undesired = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "'", '"', "@", "#", "$", "%", "^", "&", "(", ")", "<", ">", "+", "-", "=", "_", "*", ","]

class WordStorage:

    def __init__(self):
       self.storage = {}

    def put(self, word: str) -> int:
        if word == None or type(word) != str:
           return {}
        else:
           keys = []
           for k in self.storage.keys():
               keys.append(k)
           if word in keys:
              return keys.index(word)
           else:
              keys.append(word)
              num = keys.index(word)
              self.storage[word] = num
              return num

    def get_id_of(self, word: str) -> int:
        if word == None or type(word) != str or word not in self.storage.keys():
           return -1
        else:
           return self.storage[word]

    def get_original_by(self, num: int) -> str:
        if num == None or type(num) != int or num not in self.storage.values():
           return 'UNK'
        else:
           for k in self.storage.keys():
               if self.storage[k] == num:
                  return k


    def from_corpus(self, corpus: tuple):
        if corpus == None or type(corpus) != tuple or corpus == ():
                return {}
        else:
           corpus1 = []
           for i in range(0, len(corpus)):
               if corpus[i] not in self.storage.keys():
                  corpus1.append(corpus[i])
           for c in corpus1:
               self.storage[c] = corpus1.index(c)
           return self.storage


class NGramTrie:

    def __init__(self, size):
       self.gram_frequencies = {}
       self.log_probabilities = {}
       self.size = size

    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    storage_instance = WordStorage.from_corpus(corpus)
    corpus = list(corpus)
    for i in range(0, len(corpus)):
        for k in range(0, len(corpus[i])):
            corpus[i][k] = storage_instance[corpus[i][k]]
    return corpus

def split_by_sentence(text: str) -> list:
    if text == '' or text == None:
        return []
    else:
        if "\n" in text:
            text = text.replace("\n", " ")
        while "  " in text:
            text = text.replace("  ", " ")
        text = list(text)
        text = list(filter(lambda x: x not in undesired, text))
        text.remove(text[-1])
        for i in range(len(text)):
            if text[i] in punct_marks:
                text[i] = '.'
        text = ''.join(text)
        text = text.split(".")
        for i in range(0, len(text)):
            if text[i].isalpha:
                text[i] = text[i].lower()
        if len(text) == 1:
            return []
        for i in range(0, len(text)):
            text[i] = text[i].split(" ")
            for k in range(0, len(text[i]) - 1):
                if text[i][k] == '':
                    text[i].remove(text[i][k])
                text[i][k].lower()
            text[i].insert(0, "<s>")
            text[i].insert(len(text[i]), "</s>")
        return text