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
        self.counter = 0
     
    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word in self.storage:
            return -1
        self.storage[word] = self.counter
        self.counter += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.storage.keys():
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return 'UNK'
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
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
      
    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'ERROR'
        grams = []
        n = self.size

        for el in range(0, len(sentence)):
            if el <= len(sentence) - n:
                grams.append(sentence[el:el+n])

        for ngram in grams:
            self.gram_frequencies[ngram] = grams.count(ngram)
        return 'OK'

    def calculate_log_probabilities(self):
        for gram in list(self.gram_frequencies):
            all_grams = []
            gram_freq = self.gram_frequencies[gram]
            for gr in list(self.gram_frequencies):
                if gram[0] == gr[0]:
                    all_grams.append(self.gram_frequencies[gr])
            final_all_grams = sum(all_grams)
            natur_log = math.log(gram_freq / final_all_grams)
            self.gram_log_probabilities[gram] = natur_log

                
    def predict_next_sentence(self, prefix: tuple) -> list:
        
        if self.gram_log_probabilities is None or self.gram_log_probabilities == {}:
            return []
        list_pref = []
        p_ln = {}
        list_pref.append(prefix)
        
        predicted_sentence = []
        predicted_sentence.extend(list_pref)

        while(1):
            for n_gram in list(self.gram_log_probabilities):
               if list_pref == list(n_gram[:-1]):
                   p_ln[self.gram_log_probabilities[n_gram]] = n_gram

            if p_ln == {}:
                return predicted_sentence
            m = max(p_ln)
            list_pref.reverse()
            if len(list_pref) > 0: list_pref.pop()
            list_pref.reverse()
            
            list_pref.append(p_ln[m][len(p_ln[m])-1])
            predicted_sentence.append(p_ln[m][len(p_ln[m])-1])
            p_ln = {}
        return predicted_sentence 

def encode(storage_instance, corpus) -> list:
    if (storage_instance is None or corpus is None):
        return []
    encoded = []
    for sen in corpus:
        id_of_word = []
        for word in sen:
            id_of_word.append(storage_instance.get_id_of(word))
        encoded.append(id_of_word)
    return encoded


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
            if flag:
                new_text.append('</s>')
            if new_text != []:
                final_list.append(new_text)
            new_text = []
            flag = 0
                        
                        
        word = ''
    if word != '':        
        new_text.append(word)
    return final_list
