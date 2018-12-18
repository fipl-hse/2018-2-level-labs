"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.readlines()
        TEXT = " ".join(REFERENCE_TEXT)


def split_by_sentence(text: str) -> list:
    punctuation = ['.', '!', '?']
    if text is '' or text is None:
        return []

    if text[-1] not in punctuation or text[-1].isalpha():
        return []

    n_text = ''
    for el in text:
        if el.isalpha() or el == ' ':
            n_text += el
        if el in punctuation:
            n_text += '.'
    result = ''
    for index in range(0, len(n_text) - 1):
        if n_text[index] == '.':
            if n_text[index + 1].isalpha() or n_text[index + 1] == '.':
                continue
        result += n_text[index]
    result = result.split('.')
    token = []
    for el in result:
        el = el.lower()
        el = '<s> ' + el + ' </s>'
        el = el.split()
        token.append(el)
    return token


class WordStorage:
    def __init__(self):
<<<<<<< HEAD
        self.count = 100000
        self.storage = {}

    def put(self, word: str) -> int:
        if word in self.storage:
            return self.storage[word]
        
        if not isinstance(word, str):
            return 0

        for value in self.storage.values():
            if value == self.count:
                self.count += 1
                continue
        self.storage[word] = self.count
        return self.count

    def get_id_of(self, word: str) -> int:
        if word is None or not isinstance(word, str) or word not in self.storage:
            return -1
        else:
            return self.storage[word]

    def get_original_by(self, num: int) -> str:
        if not isinstance(num, int) or num < 100000:
            return 'UNK'
        for key, value in self.storage.items():
                if value == num:
                    return key

    def from_corpus(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return ''
        for el in sentence:
            self.put(el)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_log_probabilities = {}
        self.gram_frequencies = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'ERROR'

        n_gram_list = []
        result = []

        for el in range(0, (len(sentence) - 1)):
            n_gram_list.append(sentence[el:el + self.size])
        for element in n_gram_list:
            if len(element) == self.size:
                result.append(element)
        for res in result:
            if res in self.gram_frequencies:
                frequency_n = self.gram_frequencies[res]
                self.gram_frequencies[res] = frequency_n + 1
                continue
            self.gram_frequencies[tuple(res)] = 1
        return 'OK'

    def calculate_log_probabilities(self):
        engram_list = []
        counter = 0

        for key in self.gram_frequencies:
            engram_list.append(key)
            continue
=======
        self.storage = {}

    def put(self, word: str) -> int:

        if word not in self.storage and isinstance(word, str):
            code_word = hash(word)
            self.storage[word] = code_word
            return code_word

    def get_id_of(self, word: str) -> int:

        if word in self.storage:
            return self.storage.get(word)

        return -1

    def get_original_by(self, id_word: int) -> str:

        id_index = -1
        if id_word in self.storage.values():
            id_index = list(self.storage.values()).index(id_word)
        if id_index != -1:
            return list(self.storage.keys())[id_index]
        return "UNK"

    def from_corpus(self, corpus: tuple):

        if corpus and isinstance(corpus, tuple):
            for word in corpus:
                code_word = hash(word)
                self.storage[word] = code_word

        return self.storage


class NGramTrie():
    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.gram_frequencies_all = {}
        self.sentence_code_list = []

    def fill_from_sentence(self, sentence: tuple) -> str:

        if sentence and isinstance(sentence, tuple):
            self.sentence_code_list += list(sentence)

            try:
                sentence_list = list(sentence)
                for i in range(len(sentence_list) - self.size + 1):
                    count_n_gram = 0
                    n_gram = tuple(sentence_list[i:i + self.size])
                    if n_gram not in self.gram_frequencies.keys():
                        for k in range(len(self.sentence_code_list) - self.size + 1):
                            if self.sentence_code_list[k:k + self.size] == list(n_gram):
                                count_n_gram += 1
                        self.gram_frequencies[n_gram] = count_n_gram
                answer = "OK"
            except AssertionError:
                answer = "ERROR"

            return answer

    def calculate_log_probabilities(self):

        for n_gram in self.gram_frequencies:
            n_gram_part_count = 0
            n_gram_part = n_gram[:-1]
            for index, key in enumerate(list(self.gram_frequencies.keys())):
                if n_gram_part == key[:-1]:
                    n_gram_part_count += list(self.gram_frequencies.values())[index]
            probability = self.gram_frequencies[n_gram] / n_gram_part_count
            self.gram_log_probabilities[n_gram] = math.log(probability)

        return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:

        if not prefix or not isinstance(prefix, tuple):
            return []
        if len(prefix) != self.size - 1:
            return []

        n_gram_part = []
        n_gram_answer = []
        log_prob_list_number = []
        log_prob_l = sorted(self.gram_log_probabilities, key=self.gram_log_probabilities.__getitem__, reverse=True)
        for i in log_prob_l:
            log_prob_list_number += [self.gram_log_probabilities.get(i)]
        for n_gram_one in log_prob_l:
            if not n_gram_one[:-1] in n_gram_part:
                n_gram_part += [n_gram_one[:-1]]
                n_gram_answer += [n_gram_one[-1]]

        prefix_list = list(prefix)
        prefix_word = tuple(prefix)
        while True:
            if tuple(prefix_list[-self.size + 1:]) in n_gram_part:
                prefix_index = n_gram_part.index(prefix_word)
                n_gram_whole = tuple(list(prefix_word) + [n_gram_answer[prefix_index]])
                for key in log_prob_l:
                    if key == n_gram_whole:
                        prefix_list += [n_gram_answer[prefix_index]]
                        prefix_word = prefix_list[-self.size + 1:]
                        prefix_word = tuple(prefix_word)
                        break
            else:
                break

        return prefix_list
>>>>>>> upstream/master

        while counter <= (len(engram_list) - 1):
            engrams_list = []
            sum_engram = 0
            engram_now = engram_list[counter]
            for el in engram_list:
                if engram_now[:-1] == el[:-1]:
                    engrams_list.append(el)
                continue
            
            for el in engrams_list:
                sum_engram += self.gram_frequencies[el]
            logarithm = math.log(self.gram_frequencies[engram_list[counter]]/sum_engram)
            self.gram_log_probabilities[engram_list[counter]] = logarithm
            counter += 1
            continue

<<<<<<< HEAD
    def predict_next_sentence(self, prefix: tuple) -> list:
        if self.gram_log_probabilities == {}:
            return []
        prefix_list = list(prefix)
        length = len(prefix)
        counter = len(self.gram_log_probabilities)
        while counter:
            engrams = []
            for key in self.gram_log_probabilities.keys():
                if prefix_list[-length:] == list(key)[:length]:
                    engrams.append(key)
=======
def encode(storage_instance, corpus) -> list:
    code_sentences = []

    for sentence in corpus:
        code_sentence = []
        for word in sentence:
            code_word = storage_instance.get_id_of(word)
            code_sentence += [code_word]
        code_sentences += [code_sentence]

    return code_sentences
>>>>>>> upstream/master

            logarithm = []
            for el in engrams:
                logarithm.append(self.gram_log_probabilities[el])
            try:
                result = max(logarithm)
            except ValueError:
                break
            for key, value in self.gram_log_probabilities.items():
                    if result == value:
                        if key in engrams:
                            prefix_list.append(key[-1])
                            break
            counter -= 1
        return prefix_list

<<<<<<< HEAD

def encode(storage_instance, corpus) -> list:
    n_corpus = []
    sentence_id = []
    for sentence in corpus:
        for word in sentence:
            num = storage_instance.put(word)
            sentence_id.append(num)
        n_corpus.append(sentence_id)
        sentence_id = []
        continue
    return n_corpus
=======
def split_by_sentence(text: str) -> list:
    if not text:
        return []
    ord_list = (33, 63, 46)
    if ord(text[-1]) not in ord_list:
        return []

    text = text.replace('\n', " ")
    while "  " in text:
        text = text.replace("  ", " ")
    words = text.split(" ")
    while "" in words:
        words.remove("")

    sentences = []
    symbol_count = 0
    ord_list = (33, 63, 46)

    for index, word in enumerate(words):
        if symbol_count == len(sentences):
            sentences += [['<s>']]
        if not word[-1].isalpha() and index == (len(words) - 1):
            sentences[symbol_count].append(word[:-1])
            sentences[symbol_count].append("</s>")
            symbol_count += 1
        elif ord(word[-1]) in ord_list and words[index + 1][0].isupper():
            sentences[symbol_count].append(word[:-1])
            sentences[symbol_count].append("</s>")
            symbol_count += 1
        else:
            sentences[symbol_count].append(word)

    new_sentences = []

    for sentence in sentences:
        new_words = []
        for index, word in enumerate(sentence):
            new_word = ""
            if not word.isalpha() and (not word == '<s>' and not word == "</s>"):
                for i in word:
                    if i.isalpha():
                        new_word += i
                if new_word:
                    new_words.append(new_word.lower())
            else:
                new_words.append(word.lower())
        new_sentences += [new_words]

    if new_sentences[0] == ["<s>", "</s>"]:
        return []

    return new_sentences
>>>>>>> upstream/master
