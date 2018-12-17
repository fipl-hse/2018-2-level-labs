"""
Labour work #4
 TF-IDF Calculator
"""

import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    texts_list = []
    list_of_marks = [
        '.', ',', ':', '"', '`', '[', ']', '\n',
        '?', '!', '@', '&', "'", '-', '=',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '!', '?', '\n'
    ]
    if texts is None:
        return []
    for text in texts:
        if not isinstance(text, str):
            continue
        text = text.replace('<br />', ' ')
        new_text = ''
        for word in text:
            for symbol in word:
                if symbol in list_of_marks:
                    continue
                new_text += symbol
        clean_text = new_text.lower()
        words_list = clean_text.split()
        texts_list.append(words_list)
    return texts_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.corpus = corpus

    def calculate_tf(self):
        if self.corpus is None:
            return []
        for text in self.corpus:
            counter = 0
            if not isinstance(text, list):
                continue
            for word in text:
                if isinstance(word, str):
                    counter += 1
            word_tf = {}
            for word in text:
                if not isinstance(word, str):
                    continue
                nom = text.count(word)
                tf_value = nom / counter
                word_tf[word] = tf_value
            self.tf_values.append(word_tf)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus is None:
            return {}
        nom = 0
        for text in self.corpus:
            if isinstance(text, list):
                nom += 1
        for text in self.corpus:
            if not isinstance(text, list):
                continue
            for word in text:
                if not isinstance(word, str):
                    continue
                word_counter = 0
                for text2 in self.corpus:
                    if not isinstance(text2, list):
                        continue
                    if word in text2:
                        if not isinstance(word, str):
                            continue
                        word_counter += 1
                idf_value = math.log(nom / word_counter)
                self.idf_values[word] = idf_value
        return self.idf_values

    def calculate(self):
        if self.idf_values == {} or self.idf_values is None:
            return []
        if self.tf_values is [] or self.tf_values is None:
            return []
        if self.tf_idf_values is None or self.tf_idf_values is []:
            return []
        for d in self.tf_values:
            tf_idf_dict = {}
            for word in d.keys():
                tf_idf_value = d[word] * self.idf_values[word]
                tf_idf_dict[word] = tf_idf_value
            self.tf_idf_values.append(tf_idf_dict)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if self.tf_idf_values is None:
            return ()
        if self.tf_idf_values == []:
            return ()
        if document_index > len(self.corpus) - 1:
            return tuple()
        text = self.corpus[document_index]
        tf_idf_dict = self.tf_idf_values[document_index]
        storage = []
        tf_idf = 0
        significance = 0
        for word1, tf_idf_value in tf_idf_dict.items():
            if word in text:
                storage.append((tf_idf_value, word1))
        storage.sort(reverse=True)
        for index, pair in enumerate(storage):
            if word in pair:
                tf_idf = pair[0]
                significance = index
                break
        return tf_idf, significance

