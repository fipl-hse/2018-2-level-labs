"""
Labour work #3
 Building an own N-gram model
"""
from math import log


def read_from_file(path_to_file, lines_limit: int) -> str:
    my_text = ''
    count_lines = 0
    my_file = open(path_to_file, 'r')
    for line in my_file:
        if count_lines == lines_limit:
            return my_text
        my_text += line
        count_lines += 1
    my_file.close()
    return my_text


REFERENCE_TEXT = '''I love you, hope that you are alright you are the most of them, you feel it, don`t you?
there are so much things that i want to say, but there is something i can`t overcome you are you are you are you are'''


# ШАГ 1. Разбиение текста и токенизация
def split_by_sentence(text: str) -> list:
    if not isinstance(text, str):
        return []
    if text == '':
        return []

    new_text = ''
    list_of_marks = [
        '.', ',', ':', '"', '`', '[', ']',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
    ]
    good_marks = ['.', '!', '...', '?', '\n']
    result_list = list()

    for index, element in enumerate(text):
        try:
            if element in good_marks and text[index + 2].isupper():
                try:
                    new_text += '.'
                    continue
                except IndexError:
                    pass
        except IndexError:
            pass
        if element in list_of_marks:
            continue
        new_text += element
    sentences_list = new_text.split('. ')

    for sentence in sentences_list:
        sentence = sentence.lower()
        splitter = sentence.split()
        splitter.insert(0, '<s>')
        splitter.append('</s>')
        result_list.append(splitter)

    if len(result_list[0]) == 2 or len(result_list[0]) == 3:
        return []

    return result_list


# ШАГ 2. Создание хранилища
class WordStorage:
    def __init__(self):
        self.counter = 0
        self.storage = dict()

    def put(self, word: str) -> int:
        if not isinstance(word, str) or word in self.storage.keys():
            return -1

        self.storage[word] = self.counter
        self.counter += 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.storage:
            return -1
        return self.storage[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.storage.values():
            return 'UNK'

        for word, word_id in self.storage.items():
            if word_id == id:
                return word

    def from_corpus(self, corpus: tuple) -> str:
        if not isinstance(corpus, tuple):
            return 'Error'

        for word in corpus:
            self.put(word)
        return 'OK'


# ШАГ 3. Кодирование корпуса/списка предложений
#def encode(storage_instance, corpus: tuple) -> list:
    #if not isinstance(corpus, tuple):
        #return []

    #encoded_list = list()
    #for sentence in corpus:
        #inner_list = list()
        #for word in sentence:
            #inner_list.append(storage_instance[word])
        #encoded_list.append(inner_list)
    #return encoded_list

# Шаг 4. Реализация языковой модели
class NGramTrie:
    def __init__(self, scale: int):
        self.size = scale
        self.gram_frequencies = dict()
        self.gram_log_probabilities = dict()

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple):
            return 'Error'

        list_of_grams = list()

        for index, encoded_word in enumerate(sentence):
            if index == len(sentence) - 1:
                break
            list_of_grams.append((encoded_word, sentence[index + 1]))

        for gram in list_of_grams:
            self.gram_frequencies[gram] = self.gram_frequencies.get(gram, 0) + 1

        return 'OK'

    def calculate_log_probabilities(self):
        if self.size == 2:
            for gram, freq in self.gram_frequencies.items():
                general_probability = 0
                for gram_2, freq_2 in self.gram_frequencies.items():
                    if gram[0] == gram_2[0]:
                        general_probability += freq_2
                    else:
                        continue
                gram_probability = freq / general_probability
                gram_log_probability = log(gram_probability)
                self.gram_log_probabilities[gram] = gram_log_probability
        return 'OK'

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or len(prefix) != self.size - 1:
            return []

        predicted_sentence = [prefix[0], ]

        word = prefix[0]
        while True:
            probable_grams = []
            for gram, log_prob in self.gram_log_probabilities.items():
                if gram[0] == word:
                    probable_grams.append((log_prob, gram))

            if len(probable_grams) == 0:
                return predicted_sentence

            probable_grams.sort(reverse=True)
            predicted_sentence.append(probable_grams[0][1][1])
            word = probable_grams[0][1][1]

