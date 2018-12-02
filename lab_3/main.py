"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()

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
       self.gram_log_probabilities = {}
       self.size = size

    def fill_from_sentence(self, sentence: tuple) -> str:
        keys = []
        if sentence == () or type(sentence) != tuple or sentence == None:
           self.gram_frequencies = {}
        else:
           for i in range(0, len(sentence)-(self.size-1)):
               k = tuple(sentence[i: i + self.size])
               keys.append(k)
               if k[-1] == '</s>':
                  keys.append(k)
                  break
           for i in range(len(keys)):
               self.gram_frequencies[keys[i]] = keys.count(keys[i])
           return'OK'

    def calculate_log_probabilities(self):
        zn = 0
        for k in self.gram_frequencies.keys():
            zn = self.gram_frequencies[k]
            ch = self.gram_frequencies[k]
            for key in self.gram_frequencies.keys():
                if key != k and key[0:self.size-1] == k[0:self.size-1]:
                   zn += self.gram_frequencies[key]
            self.gram_log_probabilities[k] = math.log(ch/zn)
        return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:
        if prefix == None or type(prefix) != tuple:
           return []
        elif len(prefix) != self.size-1:
           return []
        else:
           lst = []
           for k in self.gram_log_probabilities.keys():
               if k[0:self.size-1] == prefix:
                  lst.append(self.gram_log_probabilities[k])
           if lst == []:
              return list(prefix)
           else:
               res = []
               val = []
               while True:
                   for k in self.gram_log_probabilities.keys():
                       if k[0:self.size-1] == prefix:
                           val.append(self.gram_log_probabilities[k])
                   if len(val) == 0:
                       break
                   else:
                       maxi = max(val)
                       for k in self.gram_log_probabilities.keys():
                           if self.gram_log_probabilities[k] == maxi and res == []:
                               for c in k:
                                   res.append(c)
                           elif self.gram_log_probabilities[k] == maxi and len(res) != 0:
                               res.append(k[-1])
                       val = []
                       maxi = 0
                       prefix = tuple(res[-(self.size-1):])
               return res


def encode(storage_instance, corpus) -> list:
    storage_instance = WordStorage.from_corpus(corpus)
    corpus = list(corpus)
    for i in range(0, len(corpus)):
        for k in range(0, len(corpus[i])):
            corpus[i][k] = storage_instance[corpus[i][k]]
    return corpus

def split_by_sentence(REFERENCE_TEXT: str) -> list:
    if REFERENCE_TEXT == '' or REFERENCE_TEXT == None:
        return []
    else:
        if "\n" in REFERENCE_TEXT:
            REFERENCE_TEXT = REFERENCE_TEXT.replace("\n", " ")
        while "  " in REFERENCE_TEXT:
            REFERENCE_TEXT = REFERENCE_TEXT.replace("  ", " ")
        REFERENCE_TEXT = list(REFERENCE_TEXT)
        REFERENCE_TEXT = list(filter(lambda x: x not in undesired, REFERENCE_TEXT))
        REFERENCE_TEXT.remove(REFERENCE_TEXT[-1])
        for i in range(len(REFERENCE_TEXT)):
            if REFERENCE_TEXT[i] in punct_marks:
                REFERENCE_TEXT[i] = '.'
        REFERENCE_TEXT  = ''.join(REFERENCE_TEXT)
        REFERENCE_TEXT = REFERENCE_TEXT.split(".")
        for i in range(0, len(REFERENCE_TEXT)):
            if REFERENCE_TEXT[i].isalpha:
               REFERENCE_TEXT[i] = REFERENCE_TEXT[i].lower()
        if len(REFERENCE_TEXT) == 1:
            return []
        for i in range(0, len(REFERENCE_TEXT)):
            REFERENCE_TEXT[i] = REFERENCE_TEXT[i].split(" ")
            for k in range(0, len(REFERENCE_TEXT[i]) - 1):
                if REFERENCE_TEXT[i][k] == '':
                   REFERENCE_TEXT[i].remove(REFERENCE_TEXT[i][k])
                REFERENCE_TEXT[i][k].lower()
            REFERENCE_TEXT[i].insert(0, "<s>")
            REFERENCE_TEXT[i].insert(len(REFERENCE_TEXT[i]), "</s>")
        return REFERENCE_TEXT