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
#changed
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






