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
    id = 0
    storage = {}
    def put(self, word: str) -> int:
        if type(word) == str:
            if word not in self.storage.keys():
                self.id = self.id + 1
                self.storage[word] = self.id
            return self.id
        else:
            return {}

    def get_id_of(self, word: str) -> int:
        if word not in self.storage.keys():
            return -1
        else:
            return self.storage.get(word)

    def get_original_by(self, id: int) -> str:
        if id in self.storage.values():
            for k, v in self.storage.items():
                if v == id:
                    return k
        else:
            return 'UNK'

    def from_corpus(self, corpus: tuple):
        try:
            if type(corpus) == tuple:
                for i in corpus:
                    st = WordStorage
                    st.put(st, i)
                return self.storage
            else:
                return {}
        except TypeError:
            return {}


class NGramTrie:
    gram_frequencies = {}
    gram_log_probabilities = {}
    def __init__(self, size):
        self.size = size
        self.length = size - 1
       
    def fill_from_sentence(self, sentence: tuple) -> str:
        try:
            if self.size == 2 and type(sentence)== tuple:
                for i in range(len(sentence) - 1):
                    t = ()
                    t = (sentence[i], sentence[i + 1])
                    if t in self.gram_frequencies.keys():
                        i = self.gram_frequencies[t]
                        self.gram_frequencies[t] = i + 1
                    else:
                        self.gram_frequencies[t] = 1
                return self.gram_frequencies
            else:
                return {}
        except TypeError:
            return {}

    def calculate_log_probabilities(self):
        dct = {}
        for k, v in self.gram_frequencies.items():
            sum = 0
            for k1, v1 in self.gram_frequencies.items():
                if k[0] == k1[0]:
                    sum += v1
            dct[k] = sum
        print(dct)
        for k3, v3 in self.gram_frequencies.items():
            v2 = dct.get(k3)
            p = v3 / v2
            res = math.log(p)
            self.gram_log_probabilities[k3] = res
        return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:
        try:
            if len(prefix) == self.length and type(prefix) == tuple:
                lst = []
                res1 = []
                for i in self.gram_log_probabilities.keys():
                    for n in i:
                        for k in prefix:
                            if n == k:
                                p = self.gram_log_probabilities.get(i)
                                lst.append(p)
                res = max(lst)
                for k1, v1 in self.gram_log_probabilities.items():
                    if v1 == res:
                        for b in k1:
                            res1.append(b)
                return res1
            else:
                return []
        except TypeError:
            return []
        except ValueError:
            prefix = list(prefix)
            return prefix


def encode(storage_instance, corpus) -> list:
        if type(corpus) == list:
           dct = storage_instance.from_corpus(storage_instance, corpus)
           for i in corpus:
               n = i.copy()
               for k in range(len(n)):
                   id = dct.get(n[k])
                   i.append(id)
           for i in corpus:
               n = i.copy()
               mid = len(n) / 2
               for k in range(len(n)):
                   while mid:
                       del i[k]
                       mid = mid - 1
           corpus = list(corpus)
           return corpus
       else:
           return [] 
    
def split_by_sentence(text: str) -> list:
        try:
            spam = " @ $ % ^ & * ( ) _ - = + , / { [ } ] ; : < > ' / # \n "
            spam = spam.split(' ')

            spam1 = ['?', '!']

            for i in text:
                if i in spam:
                    text = text.replace(i, '')
                if i in spam1:
                    text = text.replace(i, '.')

            for i in text:
                for k in range(len(text) - 1):
                    if i == '.' and text[k + 1].isupper():
                        a = []
                        a = text.split(i)
                        b = len(a) - 1
                        del a[b]

            lst1 = []
            for i in a:
                for k in i:
                    if k.isupper():
                        c = k.lower()
                        i = i.replace(k, c)
                lst = []
                lst = i.split(' ')
                print(lst)
                lst1.append(lst)

            res = []

            for i in lst1:
                res1 = []
                for k in i:
                    if k != '':
                        res1.append(k)
                res.append(res1)

            for i in res:
                i.insert(0, '<s>')
                i.append('</s>')

            return res

        except UnboundLocalError:
            return []
        except TypeError:
            return []






