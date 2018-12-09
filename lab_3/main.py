"""
Labour work #3
 Building an own N-gram model
"""
import collections
import math
import operator


if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        reference_text = f.read()
TEXT = reference_text
N = 3


def split_by_sentence(TEXT):
    if TEXT is None or not isinstance(TEXT, str):
        return []
    restr_chars = "~$%&^@*#\"{}[]\'/\n:.;!?(),<>"
    l_text = TEXT.lower()
    for i in restr_chars:
        if i in l_text:
            if i in '.!?':
                l_text = l_text.replace(i, '.')
            else:
                l_text = l_text.replace(i, '')
    for ind in enumerate(l_text):
        if l_text[ind] == '.':
            if ind + 1 >= len(l_text) or l_text[ind + 1] == ' ':
                pass
            elif l_text[ind + 1] is not None:
                l_text = l_text[:ind] + 'Ê' + l_text[ind + 1:]
            else:
                pass
    l_text = l_text.replace('Ê', '')
    cut_text = l_text.split('.')
    for sentence in enumerate(cut_text):
        cut_text[sentence] = cut_text[sentence].split()
    for element in cut_text:
        if len(element) == 0:
            cut_text.pop(cut_text.index(element))
    for element in cut_text:
        if len(element) <= 1:
            element = []
        element.append('</s>')
        element.insert(0, '<s>')
    return cut_text


class WordStorage():

    def __init__(self):
        WordStorage.storage = {}
        self.counter = 0

    def put(self, word):
        if word is None or not isinstance(word, str):
            return {}
        if word not in self.storage.keys():
            self.counter = self.counter + 1
            self.storage.update({word: self.counter})
            return self.counter
        if word in self.storage.keys():
            pass

    def get_id_of(self, word):
        if word is None or not isinstance(word, str):
            return -1
        for k, v in self.storage.items():
            if word == k:
                return v
        if word not in self.storage.keys():
            return -1

    def get_original_by(self, number):
        if number is None or not isinstance(number, int):
            return 'UNK'
        for k, v in self.storage.items():
            if number == v:
                return k
        if number not in self.storage.values():
            return 'UNK'

    def from_corpus(self, sentence):
        if sentence is None or not isinstance(sentence, tuple):
            return {}
        for elements in sentence:
            if elements not in self.storage.keys():
                ws.put(elements)


def encode(storage, cut_text):
    corpus = cut_text
    for elements in corpus:
        for syllabus in elements:
            for k, v in storage.items():
                if syllabus == k:
                    elements[elements.index(syllabus)] = v
    return corpus


class NGramTrie:

    def __init__(self, n):
        self.gram_frequencies = dict()
        self.size = n
        self.gram_log_probabilities = dict()
        self.chaotic_grams = []
        # self.candidates = dict()

    def fill_from_sentence(self, sentence):
        cnt = collections.Counter()
        chaotic_grams = []
        if sentence is () or not isinstance(sentence, tuple):
            return {}
        right = self.size
        left = 0
        while right <= len(sentence):
            chaotic_grams.append(tuple(sentence[left:right]))
            right = right + 1
            left = left + 1
            if right > len(sentence):
                break
        for gram in chaotic_grams:
            cnt[gram] += 1
        self.gram_frequencies = dict(cnt)

    def calculate_log_probabilities(self):
        for k, v in self.gram_frequencies.items():
            appropriate_values = 0
            for key, value in self.gram_frequencies.items():
                if k[:self.size - 1] == key[:self.size - 1]:
                    appropriate_values = appropriate_values + int(value)
            if appropriate_values == 0:
                self.gram_log_probabilities[k] = 0.0
            else:
                self.gram_log_probabilities[k] = math.log(v / appropriate_values)

    def predict_next_sentence(self, prefix):
        if prefix is None or not isinstance(prefix, tuple):
            return []
        if len(prefix) != self.size - 1:
            return []
        predicted_grams = set()
        postfix = prefix
        candidates = {}
        for gram, log_prob in self.gram_log_probabilities.items():
            if gram[0:self.size - 1] == postfix:
                candidates.update({gram: log_prob})
        if candidates == {}:
            return list(prefix)
        for i in range(len(self.gram_log_probabilities)):
            best_grams = []
            candidates = {}
            for gram, log_prob in self.gram_log_probabilities.items():
                if gram[0:self.size - 1] == postfix:
                    candidates.update({gram: log_prob})
            if len(candidates) < 1:
                return list(predicted_grams)
            al_eq = max(candidates.items(), key=operator.itemgetter(1))[0]
            for k, value in candidates.items():
                if value >= candidates.get(al_eq):
                    best_grams.append(k)
            perf_gram = sorted(best_grams)[0]
            for i in perf_gram:
                predicted_grams.add(i)
            postfix = perf_gram[1:]
        return list(predicted_grams)


ws = WordStorage()
ngr = NGramTrie(N)



