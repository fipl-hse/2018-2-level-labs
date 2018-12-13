# ШАГ 1. Разбиение текста и токенизация
def clean_tokenize_corpus(texts) -> list:
    if not isinstance(texts, list) or (texts is []):
        return []

    list_of_marks = [
        '.', ',', ':', '"', '`', '[', ']',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '/' '\n'
    ]
    good_marks = ['.', '!', '...', '?', '\n']
    line_breakers = '<br />'
    corpus_list = list()

    for text in texts:
        if not isinstance(text, str):
            continue
        new_text = ''
        one_text_list = list()

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
            for word in splitter:
                one_text_list.append(word)

        corpus_list.append(one_text_list)

    return corpus_list


class TfIdfCalculator:
    def __init__(self, incoming_corpus):

        if not isinstance(incoming_corpus, list):
            self.corpus = list()
        else:
            self.corpus = incoming_corpus

        self.tf_values = list()  # Лист из словарей
        self.idf_values = dict()  # Словарь из слова-значения
        self.tf_idf_values = list()  # Лист из словарей

    def calculate_tf(self):
        for splitted_text in self.corpus:

            if not isinstance(splitted_text, list):
                continue

            one_text_tf_dict = dict()

            for word in splitted_text:

                if not isinstance(word, str):
                    continue

                amount_of_words = len(splitted_text)
                word_count = 0

                for word_2 in splitted_text:
                    if word == word_2:
                        word_count += 1

                word_freq = word_count / amount_of_words
                one_text_tf_dict[word] = word_freq

            self.tf_values.append(one_text_tf_dict)
