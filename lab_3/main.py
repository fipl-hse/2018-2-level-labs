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
        self.word_id = 0

    def put(self, word: str) -> int:

        if not isinstance(word, str):
            return {}
        if word is None:
            return None
        if word in self.storage.keys():
            return self.storage[word]

        self.storage[word] = self.word_id
        self.word_id = self.word_id + 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word in self.storage.keys():
            return self.storage[word]
        else:
            return None

    def get_original_by(self, ourkod: int) -> str:
        if ourkod in self.storage.values():
            for word, kod in self.storage.items():
                if kod == ourkod:
                    return word

    def from_corpus(self, corpus: list):
        for stroka in corpus:
            for ourword in stroka:
                # if not '<' in ourword:
                self.put(ourword)

    def encode(storage_instance, corpus) -> list:
        newlist = []
        for stroka in corpus:
            newstroka = [h.get_id_of(ourword) for ourword in stroka]
            newlist.append(newstroka)
        return newlist


#t_split = []

text = REFERENCE_TEXT


def split_by_sentence(text: str) -> list:
    n = 0  # это будет счетчик вхождений точки с пробелом
    if not isinstance(text, str) or text == '':
        return []
    
    text = text.replace('! ', '. ')
    text = text.replace('? ', '. ')  # унифицировали все разделители предложений
    t_split = []
    l = len(text)
    while n != -1:              # ищем, где после ". " идет маленькая буква
        n = text.find('. ', n, l - 2)
        if n > -1:
            if not text[n + 2].isupper():
                text = text[:n] + '*' + text[n + 1:]
            n = n + 1

    t_split = text.split('. ')  # сплитнули текст на предложения

    n = -1  # это будет индекс строк нашего списка
    list_of_marks = [
    '.', ',', '!', '?', ':', '"', '`', '[', ']', '@', '&', "'", '-',
    '$', '^', '*', '(', ')', '_', '“', '”', '’', '#', '%',
    '<', '>', '*', '~', '/', '\\'
    ]
    for stroka in t_split:  # проверим каждую строчку в списке
        n = n + 1
        for mark in list_of_marks:  # проверим каждую марочку на наличие
            stroka = stroka.strip(mark)
            if mark in stroka:
                pos_mark = stroka.find(mark)
                stroka = stroka[:pos_mark] + stroka[pos_mark + 1:]
        stroka = stroka.lower()
        t_split[n] = '<s> ' + stroka + ' </s>'
        t_split[n] = t_split[n].split(' ')
    return t_split

ltext = t_split

h = WordStorage()
h.from_corpus(ltext)

class NGramTrie:
    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass




