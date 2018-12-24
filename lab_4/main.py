import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def remove_specials(text: str, key: str) -> str:
    text_splitted = text.split(key)  # делим текст по найденным key, чтобы потом склеить уже без них
    text = ''
    for stroka in text_splitted:
        if stroka.strip != '':
            text = text + ' ' + stroka
    text = text.strip()
    return text


def remove_marks(text: str) -> str:
    list_of_marks = [
        '.', ',', '!', '?', ':', '"', '`', '[', ']', '@', '&', "'",
        '$', '^', '*', '(', ')', '_', '“', '’', '#', '%', '=', '-',
        '<', '>', '~', '/', ';'
    ]
    for mark in list_of_marks:
        if mark in text:
            text = text.replace(mark, '')
    return text


def clean_tokenize_corpus(texts: list) -> list:
    if texts == None:
        return []
    corpus = []
    for text in texts:
        if not isinstance(text, str) or text == '':
            text_splitted = []
        else:
            text = remove_specials(text, '\n')
            text = remove_specials(text, '<br />')
            text = remove_marks(text)
            text = text.lower()
            text_splitted = text.split(' ')
            text_splitted = [element for element in text_splitted if element]  # убрали пустые строки из списка
        if text_splitted != []:
            corpus.append(text_splitted)
    return corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []


    def calculate_tf(self):
        if self.corpus is None or not isinstance(self.corpus, list):  # проверка корпуса в целом на соответствие
            return
        for text_splitted in self.corpus:
            if text_splitted is not None:  # проверка отдельного текста на None
                tf_dict = {}
                for word in text_splitted:
                    if isinstance(word, str):  # проверка отдельного элемента текста (слово или нет)
                        try:
                            tf_dict[word] += 1
                        except:
                            tf_dict[word] = 1
                len_text = len(text_splitted)
                for word in tf_dict.keys():
                    tf_dict[word] = tf_dict[word] / len_text
                self.tf_values.append(tf_dict)

    def calculate_idf(self):
        if self.corpus is None or not isinstance(self.corpus, list):  # проверка корпуса в целом на соответствие
            return
        self.calculate_tf()  # работаем со словарем ТФ, т.к. в нем уже убраны дубликаты слов в каждом тексте
        if self.tf_values:
            D = len(self.tf_values)
            for dict in self.tf_values:
                for word in dict.keys():
                    try:
                        self.idf_values[word] += 1
                    except:
                        self.idf_values[word] = 1
            for word in self.idf_values.keys():
                self.idf_values[word] = math.log(D / self.idf_values[word])

    def calculate(self):
        if self.corpus is None or not isinstance(self.corpus, list):  # проверка корпуса в целом на соответствие
            return
        if self.tf_values and self.idf_values:
            for tf_dict in self.tf_values:
                tf_idf_dict = {}
                for word in tf_dict.keys():
                    tf_idf_dict[word] = tf_dict[word] * self.idf_values[word]
                self.tf_idf_values.append(tf_idf_dict)

    def report_on(self, word, doc_index):
        if self.corpus is None or not isinstance(self.corpus, list):    # проверка корпуса в целом на соответствие
            return
        if word is None or not isinstance(word, str):                   # проверка слова на соответствие
            return
        if doc_index is None or not isinstance(doc_index, int):         # проверка номера текста на соответствие
            return
        if doc_index > len(self.corpus) - 1:                    # проверка номера текста на непревышение числа текстов
            return()
        if not self.tf_idf_values:
            return()

        tf_idf_dict = self.tf_idf_values[doc_index]
        word_tf_idf = tf_idf_dict[word]

        our_values = [element for element in tf_idf_dict.values()]
        our_values = set(our_values)
        our_values = list(our_values)
        our_values.sort(reverse = True)

        word_rating = our_values.index(word_tf_idf)
        return(word_tf_idf, word_rating)


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
word_1 = 'good'
word_2 = 'and'
print(word_1, tf_idf.report_on(word_1, 0))
print(word_2, tf_idf.report_on(word_2, 1))
