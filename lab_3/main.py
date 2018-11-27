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
        if word == None or type(word) != 'str' or word in self.storage.keys():
           return {}
        else:
           self.storage[word] = num
           return num

    def get_id_of(self, word: str) -> int:
        if word in self.storage.keys() and word != '' and word != None and type(word) == "str":
            return self.storage[word]
        elif word == '' or word == None or type(word) != "str":
            return -1
        else:
            return None

    def get_original_by(self, num: int) -> str:
        if num == None or type(num) != 'int' or num not in self.storage.values():
           return 'UNK'
        elif num in self.storage.values():
           for k in self.storage.keys():
               if self.storage[k] == num:
                  return k
        else:
            return None

    def from_corpus(self, corpus: tuple):
        for i in range(0, len(corpus)):
            for k in range(0, len(corpus[i])):
                word = corpus[i][k]
                WordStorage.put(self, word)
        return self.storage


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
    if text == '' or text == None:
       return []
    else:
       text = list(text)
       text = list(filter(lambda x: x not in undesired, text))
       text.remove(text[-1])
       for i in range(1, len(text) - 1):
           if text[i] == " " and text[i - 1] == " ":
              text.remove(text[i])
           if text[i] in punct_marks:
              text[i] = '.'
       text = ''.join(text)
       text = text.split(".")
       for i in range(0, len(text)):
           if text[i].isalpha:
              text[i] = text[i].lower()
           text[i] = text[i].split(" ")
           for k in range(0, len(text[i]) - 1):
               if text[i][k] == '':
                  text[i].remove(text[i][k])
               text[i][k].lower()
           text[i].insert(0, "<s>")
           text[i].insert(len(text[i]), "</s>")
    return text

