import math


# ШАГ 1. Разбиение корпуса и токенизация
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
    corpus_list = list()

    for text in texts:
        if not isinstance(text, str):
            continue

        text = text.replace('<br />', ' ')
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


# Шаг 2. Объявление класса и методов. TF-IDF показатели.
class TfIdfCalculator:
    def __init__(self, incoming_corpus):

        if not isinstance(incoming_corpus, list):
            self.corpus = list()
        else:
            self.corpus = incoming_corpus

        self.tf_values = list()
        self.idf_values = dict()
        self.tf_idf_values = list()
        self.file_names = ['5_7', '15_2', '10547_3', '12230_7']

    def calculate_tf(self):
        for splitted_text in self.corpus:
            if not isinstance(splitted_text, list):
                continue

            one_text_tf_dict = dict()
            total_words = 0

            for word in splitted_text:
                if isinstance(word, str):
                    total_words += 1

            for word in splitted_text:
                if not isinstance(word, str):
                    continue

                word_count = 0

                for word_2 in splitted_text:
                    if word == word_2:
                        word_count += 1

                word_freq = word_count / total_words
                one_text_tf_dict[word] = word_freq

            self.tf_values.append(one_text_tf_dict)

    def calculate_idf(self):
        amount_of_texts = 0

        for splitted_text in self.corpus:
            if isinstance(splitted_text, list):
                amount_of_texts += 1

        for splitted_text in self.corpus:
            if not isinstance(splitted_text, list):
                continue

            for word in splitted_text:
                if not isinstance(word, str):
                    continue

                word_counter = 0

                for splitted_text_2 in self.corpus:
                    if not isinstance(splitted_text_2, list):
                        continue
                    if word in splitted_text_2:
                        word_counter += 1

                self.idf_values[word] = math.log(amount_of_texts / word_counter)

    def calculate(self):
        if not isinstance(self.tf_values, list) or not isinstance(self.idf_values, dict) or (len(self.idf_values) == 0):
            return []

        for tf_dict in self.tf_values:

            one_tf_idf_dict = dict()

            for word, word_tf in tf_dict.items():

                for word_2, word_idf in self.idf_values.items():
                    if word == word_2:
                        one_tf_idf_dict[word] = word_tf * word_idf

            self.tf_idf_values.append(one_tf_idf_dict)

    def report_on(self, word, document_index):
        if not isinstance(self.tf_idf_values, list):
            return ()
        if (document_index > len(self.corpus) - 1) or (len(self.tf_idf_values) == 0):
            return ()

        current_text = self.corpus[document_index]
        current_tf_idf_dict = self.tf_idf_values[document_index]
        word_tf_idf_list = list()

        if word not in current_tf_idf_dict.keys():
            return ()

        for word_2 in current_text:
            if word_2 in current_tf_idf_dict:
                word_tf_idf_list.append((current_tf_idf_dict[word_2], word_2))
            else:
                word_tf_idf_list.append((0, word_2))

        word_tf_idf_list.sort(reverse=True)

        for index, pair in enumerate(word_tf_idf_list):
            if pair[1] == word:
                position = index
                break

        result = (current_tf_idf_dict[word], position)
        return result

    def dump_report_csv(self):
        file = open(r'C:\Users\Andrew\Desktop\2018-2-level-labs\lab_4\report.csv', 'w', encoding='UTF-8')
        first_line = 'word,tf_text_1,tf_text_2,idf,tf_idf_text_1,tf_idf_text_2'
        file.write(first_line + '\n')
        file.close()
