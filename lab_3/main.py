"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()

def split_by_sentence(text: str) -> list:

    if not isinstance(text, str) or text == '':
        return []

    text_div_n = text.split('\n')  # делим текст по \n, чтобы потом склеить уже без них
    text = ''
    for stroka in text_div_n:
        if stroka.strip != '':
            text = text + ' ' + stroka

    text = text.replace('! ', '. ')
    text = text.replace('? ', '. ')  # унифицировали все разделители предложений

    l = len(text)

    n = 0               # это будет счетчик вхождений точки с пробелом
                        # ищем, где после ". " идет маленькая буква
    while n != -1:
        n = text.find('. ', n, l - 2)
        if n > -1:
            if not text[n + 2].isupper() and text[n + 2] != ' ':
                text = text[:n] + '*' + text[n + 1:]
            n = n + 1

    t_split = text.split('. ')  # сплитнули текст на предложения
                                # далее следует удаление "марок"

    list_of_marks = [
        '.', ',', '!', '?', ':', '"', '`', '[', ']', '@', '&', "'",
        '$', '^', '*', '(', ')', '_', '“', '’', '#', '%', '='
        '<', '>', '~', '/', '\\'
        ]

    n = -1                  # это будет индекс строк нашего списка
    for stroka in t_split:  # проверим каждую строчку в списке
        n = n + 1
        for mark in list_of_marks:  # проверим каждую марочку на наличие
            stroka = stroka.strip(mark)
            if mark in stroka:
                stroka = stroka.replace(mark, '')
        stroka = stroka.lower()
        if stroka.find(' ', 0) == -1:  # проверка на строки из одного слова (not sentence)
            stroka = []
        t_split[n] = stroka

    t_split = [element for element in t_split if element]   # убрали пустые строки из списка

    n = -1
    for stroka in t_split:
        n = n + 1
        t_split[n] = '<s> ' + stroka + ' </s>'
        t_split[n] = t_split[n].split(' ')
        stroka = [element for element in t_split[n] if element]
        t_split[n] = stroka

    return t_split

# ======================================================================

class WordStorage:

    def __init__(self):     # Задаем свойства для объекта класса WordStorage -
        self.storage = {}   # пустой словарь,
        self.id = 0    # ноль для переменной, в которой будет значение словаря (id очередного слова)


    def put(self, word: str) -> int:

        if not isinstance(word, str):
            return
        if word in self.storage.keys():
            return self.storage[word]

        self.id = self.id + 1
        self.storage[word] = self.id
        return self.storage[word]


    def get_id_of(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word not in self.storage.keys():
            return -1
        return self.storage[word]


    def get_original_by(self, our_id: int) -> str:
        if isinstance(our_id, int) and our_id in self.storage.values():
            for word, id in self.storage.items():
                if id == our_id:
                    return word
        return 'UNK'


    def from_corpus(self, corpus: tuple):
        if corpus == None:
            return
        if isinstance(corpus, list) or isinstance(corpus, tuple):       # проверяем, что корпус - тупл или список
            corpus = tuple(corpus)                                      # на всякий случай превращаем в тупл
            for element in corpus:
                if isinstance(element, str):                            # проверяем тип элемента корпуса  - если одиночное слово,
                    self.put(element)                                   # то сразу кладем элемент в наш словарь;
                if isinstance(element, list) or isinstance(element, tuple):     # если элемент - предложение (список или тупл),
                    for word in element:                                        # то берем его по словечку -
                        self.put(word)                                          # и по словечку кладем в словарь

# ====== кончились коды класса WordStorage ===============================

def encode(storage_instance, corpus) -> list:
    newlist = []
    id_of_word = []
    if corpus == None:
        return
    for sentence in corpus:
        for word in sentence:
            id_of_word.append(storage_instance.put(word))
            newlist.append(id_of_word)
            id_of_word = []
        continue
    return newlist

# ==========================================================================

class NGramTrie:

    def __init__(self, s):                     # Задаем свойства для объекта класса НГрамТри
        self.size = s                          # число слов в н-грамме
        self.gram_frequencies = {}          # словарь для н-грамм с частотами
        self.gram_log_probabilities = {}    # словарь для н-грамм с лог. вероятностями


    def fill_from_sentence(self, sentence: tuple) -> str:
        N = self.size
        if N < 1 or N == None or sentence == None:                                  # ну так, на всякий случай
            return ('ERROR')
        if not isinstance(sentence, tuple):                                         # ну мало ли, всякое бывает
            return ('ERROR')
        if len(sentence) - 1 < N:                                                   # если предложение коротковато
            return ('ERROR')

        last_n_gram_start = len(sentence) - N + 1
        for i in range(0, last_n_gram_start):
            n_gram_cur = sentence[i: i + N:]
            try:
                self.gram_frequencies[n_gram_cur] += 1
            except KeyError:
                self.gram_frequencies[n_gram_cur] = 1

        return('OK')

    def calculate_log_probabilities(self):
        prefix_freq = {}

        for n_gram in self.gram_frequencies.keys():
            N = self.size
            prefix = n_gram[0: N - 1]
            try:
                prefix_freq[prefix] += self.gram_frequencies[n_gram]
            except KeyError:
                prefix_freq[prefix] = self.gram_frequencies[n_gram]

        for n_gram in self.gram_frequencies.keys():
            prefix = n_gram[0: N - 1]
            self.gram_log_probabilities[n_gram] = math.log((self.gram_frequencies[n_gram] / prefix_freq[prefix]))

    def predict_next_sentence(self, prefix: tuple) -> list:
        bricks = []
        n_gram = self.predict_next_n_gram(prefix)
        sentence = n_gram                               # на тот случай, если найдем не больше одной н-граммы

        while isinstance(n_gram, list) and n_gram != [] and n_gram != list(prefix):
            bricks.append(n_gram)
            hvost = tuple(n_gram[-len(prefix)::])
            prefix = hvost
            n_gram = self.predict_next_n_gram(prefix)

        if bricks != []:
            sentence = bricks[0]
            for n_gram in bricks[1:]:
                sentence.append(n_gram[-1])
        print (sentence, 'это сентенс')
        return sentence


    def predict_next_n_gram(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or prefix == None:
            return[]
        N = len(prefix) + 1
        if N != self.size:  # Если длина префикса не соответствует N-1
            return []
        n_grams_on_prefix = {}
        for n_gram in self.gram_log_probabilities.keys():
            if prefix == n_gram[0: N-1:]:
                print ('N_GRAM CATCHED!!!', n_gram, "     Log_prob. ", self.gram_log_probabilities[n_gram])
                n_grams_on_prefix[n_gram] = self.gram_log_probabilities[n_gram]
                #break
        if n_grams_on_prefix == {}:
            return list(prefix)
        m = max(n_grams_on_prefix.values())
        print('Max.  log. probability - ', m)
        our_tuple = (get_key(n_grams_on_prefix, m))
        return list(our_tuple)

# ====== кончились коды класса NGramTrie ===============================

def get_key(our_dict: dict, our_id) -> tuple:
    if our_id in our_dict.values():
        for key, id in our_dict.items():
            if id == our_id:
                return key
    return 'UNK'

# ======================================================================

#n_symbols = 1000

sentences = split_by_sentence(REFERENCE_TEXT)  # ref text is first 500 lines from original text
#print(len(REFERENCE_TEXT))
print ('Splitting completed')

ws = WordStorage()
for sentence in sentences:
    ws.from_corpus(tuple(sentence))
print ('Dict filling completed')

ngram = NGramTrie(4)
# for sentence in sentences:
encoded = encode(ws, sentences)
print ('Encoding completed')
print()

for enc in encoded:
    ngram.fill_from_sentence(tuple(enc))
ngram.calculate_log_probabilities()
word1 = ws.get_id_of('she')
word2 = ws.get_id_of('will')
word3 = ws.get_id_of('not')
#print(word1, word2, word3)
prefix = (word1, word2, word3)
print ('Префикс - ', prefix)

words = ngram.predict_next_n_gram(prefix)
print()
print('words', words)
predicted_sent = ''
for word in words:
    word_for_user = ws.get_original_by(word)
    if word_for_user != '</s>':
        predicted_sent = predicted_sent + ' ' + word_for_user
print (predicted_sent[1:])
