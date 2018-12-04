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
        self.storage = dict()
        self.count = 0

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word in self.storage:
            return -1
        self.storage[word] = self.count
        self.count += 1
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

    def from_corpus(self, corpus: tuple) -> str:
        if not isinstance(corpus, tuple):
            return 'UNK'

        for word in corpus:
            if word not in self.storage:
                self.storage[word] = self.count
                self.count += 1
            else:
                continue

        return 'OK'


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = dict()
        self.gram_log_probabilities = dict()


    def fill_from_sentence(self, sentence: tuple) -> str:

        if not isinstance(sentence, tuple):
            return 'ERROR'
        list_of_grams = list()
        if self.size == 2:
            for i, e in enumerate(sentence):
                if len(sentence) == i + 1:
                    break
                list_of_grams.append((e, sentence[i + 1]))
        if self.size == 3:
            for i, e in enumerate(sentence):
                if len(sentence) == i + 2:
                    break
                list_of_grams.append((e, sentence[i + 1], sentence[i + 2]))

        for gram in list_of_grams:
            if gram in self.gram_frequencies:
                self.gram_frequencies[gram] += 1
            else:
                self.gram_frequencies[gram] = 1
        return 'OK'


    def calculate_log_probabilities(self):


        if self.size == 2:
            for i, e in self.gram_frequencies.items():
                summ = 0
                for m, n in self.gram_frequencies.items():
                    if i[0] == m[0]:
                        summ += n
                    else:
                        continue
                a = math.log(e / summ)
                self.gram_log_probabilities[i] = a
        if self.size == 3:
            for i, e in self.gram_frequencies.items():
                summ = 0
                for m, n in self.gram_frequencies.items():
                    if (i[0] == m[0]) and (i[1] == m[1]):
                        summ += n
                    else:
                        continue
                a = math.log(e / summ)
                self.gram_log_probabilities[i] = a

        return 'OK'

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple):
            return []
        if len(prefix) != self.size - 1:
            return []
        sentence = []
        if self.size == 2:
            word = prefix[0]
            sentence.append(word)
            while True:
                next_gram = list()
                for gram, gram_prob in self.gram_log_probabilities.items():
                    if gram[0] == word:
                        next_gram.append((gram_prob, gram))

                if len(next_gram) == 0:
                    return sentence

                next_gram.sort(reverse=True)
                sentence.append(next_gram[0][1][1])
                word = next_gram[0][1][1]

        if self.size == 3:
            words = [prefix[0], prefix[1]]
            sentence = [prefix[0], prefix[1], ]
            while True:
                next_gram = list()
                for gram, gram_prob in self.gram_log_probabilities.items():
                    if (gram[0] == words[0]) and (gram[1] == words[1]):
                        next_gram.append((gram_prob, gram))
                if len(next_gram) == 0:
                    return sentence
                next_gram.sort(reverse=True)
                sentence.append(next_gram[0][1][2])
                words[0] = next_gram[0][1][1]
                words[1] = next_gram[0][1][2]
                
                
def encode(storage_instance, corpus) -> list:
    corpus_of_sentences = []
    for sentence in corpus:
        id_sentence = []
        for word in sentence:
            quantity = storage_instance.put(word)
            id_sentence.append(quantity)
        corpus_of_sentences.append(id_sentence)
    return corpus_of_sentences
   
   
def split_by_sentence(text: str) -> list:
    if not isinstance(text, str):
        return []
    if text == None or text == '':
        return []  
     
    new_text = ''
    end_marks = ['.', '\n', '!', '?', '...']
    marks = ['.', ',', ':', '"', '`', '[', ']',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n']
    
    sentences = []
    list_with_words = []
    for i, e in enumerate(text):
        if e in end_marks:
            if text[i + 2].isupper():
                new_text += '.' + text[sentence + 1]
                continue
        if e in marks:
            continue
        new_text += e
    new_text = new_text.lower()
    sentences = new_text.split('. ')

    for i in sentences:
        i = i.split()
        i.insert(0, '<s>')
        i.append('</s>')
        list_with_words.append(i)
    if (len(list_with_words[0]) == 2) or (len(list_with_words[0]) == 3):
        return []
     
    return list_with_words
