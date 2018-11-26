"""
Labour work #3
 Building an own N-gram model
"""

import math
import string
REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.currentId = 1
        self.storage = {}

    def put(self, word):
        if word is not None and isinstance(word, str):
            if word not in self.storage:
                self.storage[word] = self.currentId
                self.currentId += 1
                return self.currentId - 1
            else:
                return self.storage[word]

    def get_id_of(self, word: string) -> int:
        if word is not None and isinstance(word, str):
            return self.storage.get(word, -1)
        else:
            return -1

    def get_original_by(self, id: int) -> string:
        if id is not None and isinstance(id, int):
            word = [key for key in self.storage if self.storage.get(key) == id]
            return word[0] if word != [] else 'UNK'
        else:
            return 'UNK'

    def from_corpus(self, corpus: tuple):
        if not corpus == () and corpus is not None and isinstance(corpus, tuple):
            for word in corpus:
                self.put(word)


class NGramTrie:

    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        self. gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence is None or sentence == () or not isinstance(sentence, tuple):
            return 'Error'
        for i in range(len(sentence) - self.size + 1):
            cur_tuple = tuple(sentence[i:i + self.size])
            if cur_tuple in self.gram_frequencies:
                self.gram_frequencies[cur_tuple] += 1
            else:
                self.gram_frequencies[cur_tuple] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        if not self.gram_frequencies == {}:

            for curGram in self.gram_frequencies:
                # bi
                if self.size == 2:
                    cur_sum = 0
                    for gram in self.gram_frequencies:
                        if gram[0] == curGram[0]:
                            cur_sum += self.gram_frequencies[gram]
                    self.gram_log_probabilities[curGram] = math.log(
                        self.gram_frequencies[curGram] / cur_sum)
                # tri
                if self.size == 3:
                    cur_sum = 0
                    for gram in self.gram_frequencies:
                        if gram[0] == curGram[0] and gram[1] == curGram[1]:
                            cur_sum += self.gram_frequencies[gram]
                    self.gram_log_probabilities[curGram] = math.log(
                        self.gram_frequencies[curGram] / cur_sum)

    def predict_next_sentence(self, prefix: tuple) -> list:
        if prefix is None or prefix == () or not isinstance(prefix, tuple):
            return []
        if not len(prefix) == self.size - 1:
            return []
        prefix_list = [prefix[0]]
        # bi
        if self.size == 2:
            while True:
                cur_log = []
                for gram in self.gram_log_probabilities:
                    if gram[0] == prefix[0]:
                        cur_log.append(
                            (self.gram_log_probabilities[gram], gram))
                if not cur_log == []:
                    prefix = ((max(cur_log)[1])[1],)
                    prefix_list.append(prefix[0])
                    cur_log.append(prefix)
                else:
                    return prefix_list
        # tri
        prefix_list = [prefix[0], prefix[1]]
        if self.size == 3:
            while True:
                cur_log = []
                for gram in self.gram_log_probabilities:
                    if gram[0] == prefix[0] and gram[1] == prefix[1]:
                        cur_log.append(
                            (self.gram_log_probabilities[gram], gram))
                if not cur_log == []:
                    prefix = (max(cur_log)[1])[1:3]
                    prefix_list.append(prefix[-1])
                    cur_log.append(prefix)
                else:
                    return prefix_list


def encode(storage_instance, corpus) -> list:
    new_list = []
    new_line = []
    for line in corpus:
        new_line.append('<s>')
        new_line += [storage_instance.get_id_of(word)
                    for word in line[1:len(line) - 1]]
        new_line.append('</s>')
        new_list.append(new_line)
        new_line = []
    return new_list


def split_by_sentence(text: str) -> list:
    if text is None and not isinstance(text, str):
        return []

    punctuation = '"#$%&\'()*+,-/:;<=>@[\\]^_`{|}~'
    punctuation_end = '!.?'
    splited_text = text.translate(str.maketrans('', '', punctuation)).split()
    if len(splited_text) < 2:
        return([])

    splited_text[0] = splited_text[0].lower()
    new_list = []
    cur_list = ['<s>']
    for i, word in enumerate(splited_text):
        if i == 0:
            i = 1
        if word[0].isupper() and splited_text[i - 1][-1] in punctuation_end:
            cur_list.append('</s>')
            new_list.append(cur_list)
            cur_list = ['<s>']
            cur_list.append(
                word.lower().translate(
                    str.maketrans(
                        '', '', punctuation_end)))
        else:
            cur_list.append(
                word.lower().translate(
                    str.maketrans(
                        '', '', punctuation_end)))
    cur_list.append('</s>')
    new_list.append(cur_list)
    return new_list
