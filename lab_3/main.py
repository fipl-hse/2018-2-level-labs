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
        if not isinstance(prefix, tuple) or not prefix:
            return []
        if len(prefix) != self.size - 1:
            return []
        if self.size == 2:
            sentence = [prefix[0], ]
            word = prefix[0]
            result = []
            for key, value in self.gram_log_probabilities.items():
                if key[0] == word:
                    result.append((value, key))
            if len(result) == 0:
                return sentence
            result.sort(reverse=True)
            sentence.append(result[0][1][1])
            word = result[0][1][1]
        elif self.size == 3:

            sentence = [prefix[0], prefix[1], ]
            word = [prefix[0], prefix[1]]
            while True:
                result = []
                for key, value in self.gram_log_probabilities.items():
                    if key[0] == word[0] and key[1] == word[1]:
                        result.append((value, key))
                if len(result) == 0:
                    return sentence
                result.sort(reverse=True)
                sentence.append(result[0][1][2])
                word[0] = result[0][1][1]
                word[1] = result[0][1][2]
def encode(storage_instance, corpus) -> list:
    corpus_of_sentences = []
    for sentence in corpus:
        id_sentence = []
        for word in sentence:
            quantity = storage_instance.put(word)
            id_sentence.append(quantity)
        corpus_of_sentences.append(id_sentence)
    return corpus_of_sentences


def split_by_sentence(text):
    punct = ['.', '?', '!']
    if text is '':
        return []
    if text[-1] not in punct:
        return []

    new_text = ''
    for sym in text:
        if sym is ' ' or sym.isalpha():
            new_text += sym
        if sym in punct:
            new_text += '.'

    sentences = ''
    for sym in range(0, len(new_text) - 1):
        if new_text[sym] is '.':
            if new_text[sym + 1].isalpha():
                continue
            if new_text[sym + 1] is '.':
                continue
        sentences += new_text[sym]

    sentences = sentences.split('.')

    list_with_words = []
    for k in sentences:
        s = k.lower()
        r = '<s> ' + s + ' </s>'
        r.split()
        token.append(r)
    if (len(list_with_words[0]) == 2) or (len(list_with_words[0]) == 3):
        return []

    return list_with_words
