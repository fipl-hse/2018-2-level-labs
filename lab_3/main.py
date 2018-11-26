"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()

def split_by_sentence(text):
    punctuation = ['.', '?', '!']
    if text is '' or text is None:
        return []
    if text[-1] not in punctuation:
        return []
     
    new_text = ''
    for el in text:
        if el is ' ' or el.isalpha():
            new_text += el
        if el in punctuation:
            new_text += '.'
          
    result = ''
    for el in range(0, len(new_text)-1):
        if new_text[el] is '.':
            if new_text[el+1].isalpha():
                continue
            if new_text[el+1] is '.':
                continue
        result += new_text[el]
    
    result = result.split('.')
    token = []
    for el in result:
        el_l = el.lower()
        el_s = '<s> ' + el_l + ' </s>'
        el_fin = el_s.split()
        token.append(el_fin)
     return token
    
class WordStorage:
    def __init__(self):
        self.count = 111111
        self.store = {}

    def put(self, word):
        if word in self.store:
            return self.store[word]

        for value in self.store.values():
            if value == self.count:
                self.count += 1
                continue

        self.store[word] = self.count
        return self.count

    def get_id_of(self, word):
        if word is None or not type(word) != str or word not in self.store:
            return None
        return self.store[word]

    def get_original_by(self, number):
        if type(number) != int or number < 111111:
            return 'UNK'

        for key, value in self.store.items():
            if value == number:
                return key
        return 'UNK'

    def from_corpus(self, sentence):
        if type(sentence) == tuple:
            return ''

        for el in sentence:
            self.put(el)


def encode(store_instance, corpus):
    corpus_n = []
    sentence_id = []

    for sentence in corpus:
        for word in sentence:
            number = store_instance.put(word)
            sentence_id.append(number)
        corpus_n.append(sentence_id)
        sentence_id = []
        continue
    return corpus_n


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.log_prob = {}
        self.frequency = {}

    def fill_from_sentence(self, sentence):
        if type(sentence) != tuple:
            return 'ERROR'

        n_gram_list = []
        for el in range(0, (len(sentence)-1)):
            n_gram_list.append(sentence[el:el+self.size])
        result = []

        for n_gram in n_gram_list:
            if len(n_gram) == self.size:
                result.append(n_gram)

        for n_gram in result:
            frequency = n_gram_list.count(n_gram)
            self.frequency[tuple(n_gram)] = frequency
        return 'OK'

    def calculate_log_probabilities(self):
        engram_list = []
        for key in self.frequency:
            engram_list.append(key)
            continue

        count = 0
        while count <= (len(engram_list) - 1):
            engrams_list = []
            for engram in engram_list:
                if engram_list[count][:-1] == engram[:-1]:
                    engrams_list.append(engram)
                continue
            sum_elist = 0

            for engram in engrams_list:
                sum_elist += self.frequency[engram]
            log = math.log(self.frequency[engram_list[count]] / sum_elist)
            self.log_prob[engram_list[count]] = log
            count += 1
            continue

    def predict_next_sentence(self, prefix):
        if self.log_prob == {}:
            return []

        prefix_list = list(prefix)
        length = len(prefix)
        count = len(self.log_prob)
        while count:
            engrams = []
            for key, value in self.log_prob.items():
                if prefix_list[-length:] == list(key)[:length]:
                    engrams.append(key)
            logs = []

            for engram in engrams:
                logs.append(self.log_prob[engram])
                res = max(logs)

            for key, value in self.log_prob.items():
                if res == value:
                    prefix_list.append(key[-1])
            count -= 1
        return prefix_list
