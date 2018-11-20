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


#REFERENCE_TEXT = read_from_file('C:\\Users\\Andrew\\Desktop\\2018-2-level-labs\\lab_3\\not_so_big_reference_text.txt',
                                #100)
#print(REFERENCE_TEXT)
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
                    new_text += '.' + text[index + 1]
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
        splitted = sentence.split()
        result_list.append(splitted)

    if [] in result_list:
        return []
    return result_list


# ШАГ 2. Создание хранилища
class WordStorage:
    def __init__(self):
        self.counter = 0
        self.storage = dict()

    def put(self, word: str) -> int:
        if not isinstance(word, str) or word in self.storage:
            return 'Error'
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
            if word in self.storage:
                continue
            self.storage[word] = self.counter
            self.counter += 1
        return 'OK'
        #for sentence in corpus:
            #for word in sentence:
                #if word in self.storage:
                    #continue
                #self.storage[word] = self.counter
                #self.counter += 1
        #return 'OK'


raw_storage = WordStorage()
raw_storage.from_corpus(('<s>', 'mary', 'wanted', 'to', 'to', 'swim', '</s>'))
print(raw_storage.storage)


# ШАГ 3. Кодирование корпуса/списка предложений
def encode(storage_instance, corpus) -> list:
    encoded_list = list()
    for sentence in corpus:
        inner_list = list()
        inner_list.append(raw_storage.get_id_of('<s>'))
        for word in sentence:
            inner_list.append(storage_instance[word])
        inner_list.append(raw_storage.get_id_of('</s>'))
        encoded_list.append(inner_list)
    return encoded_list


#raw_storage.from_corpus(tuple(split_by_sentence(REFERENCE_TEXT)))
raw_storage.put('<s>')
raw_storage.put('</s>')

encoded_text = encode(raw_storage.storage, split_by_sentence(REFERENCE_TEXT))

#print(raw_storage.word_id_dict)
#print(encoded_text)


class NGramTrie:
    def __init__(self, scale: int):
        self.size = scale
        self.gram_frequencies = dict()
        self.gram_log_probabilities = dict()

    def fill_from_sentence(self, sentence: tuple) -> str:
        list_of_grams_text = list()
        
        for sentence in encoded_text:
            for index, word in enumerate(sentence):
                if len(sentence) <= 1:
                    list_of_grams_text.append((raw_storage.get_id_of('<s>'), word))
                    list_of_grams_text.append((word, raw_storage.get_id_of('</s>')))
                    break
                if index == 0:
                    list_of_grams_text.append((raw_storage.get_id_of('<s>'), word))
                    list_of_grams_text.append((word, sentence[index + 1]))
                    continue
                if index == len(sentence) - 1:
                    list_of_grams_text.append((word, raw_storage.get_id_of('</s>')))
                    break
                list_of_grams_text.append((word, sentence[index + 1]))

        for gram in list_of_grams_text:
            if gram in self.gram_frequencies:
                continue
            for encoded_sentence in encoded_text:
                for index, encoded_word in enumerate(encoded_sentence):
                    if index == len(encoded_sentence) - 1:
                        break
                    if (gram[0] == encoded_word) and (gram[1] == encoded_sentence[index + 1]):
                        self.gram_frequencies[gram] = self.gram_frequencies.get(gram, 0) + 1
        return 'OK'

    def calculate_log_probabilities(self):
        for gram, freq in self.gram_frequencies.items():
            general_probability = 0
            for gram_2 , freq_2 in self.gram_frequencies.items():
                if gram[0] == gram_2[0]:
                    general_probability += freq_2
                else:
                    continue
            gram_probability = freq / general_probability
            gram_log_probability = log(gram_probability)
            self.gram_log_probabilities[gram] = gram_log_probability
        return 'OK'


#NGram_raw = NGramTrie(2)
#NGram_raw.fill_from_sentence(encoded_text[0])
#NGram_raw.calculate_log_probabilities()
#print(raw_storage.word_id_dict)
#print(NGram_raw.gram_frequencies)
#print(NGram_raw.gram_log_probabilities)
