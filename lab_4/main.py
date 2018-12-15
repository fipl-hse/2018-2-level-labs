import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    matrix_of_tokenized_texts = []
    if texts:
        for text in texts:
            if text and isinstance(text, str):
                import re
                list_of_sentences = []
                # разбиваем текст по пробелам и разрывам строк:
                prepared_text = re.split(r' |<br ', text.lower())
                for element in prepared_text:
                    new_word = ''
                    for el_element in enumerate(element):  # вводим дополнительный цикл, где избавляемся от лишнего "мусора"
                        if el_element[1] in 'qwertyuioplkjhgfdsazxcvbnm':
                            new_word += el_element[1]
                    if new_word:
                        list_of_sentences.append(new_word)
                matrix_of_tokenized_texts.append(list_of_sentences)
    return matrix_of_tokenized_texts



class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus_of_texts
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus and isinstance(self.corpus, list):
            for text in self.corpus:
                if text:
                    dict_of_freq = {}
                    for word in text:
                        if isinstance(word, str):
                            if word not in dict_of_freq:
                                dict_of_freq[word] = 1
                            else:
                                new_value = dict_of_freq[word] + 1
                                dict_of_freq[word] = new_value
                    for word, value in dict_of_freq.items():
                        dict_of_freq[word] = value / len(text)
                    self.tf_values.append(dict_of_freq)

    def calculate_idf(self):
        if self.corpus and isinstance(self.corpus, list):
            for text in self.corpus:
                if text:
                    for word in text:
                        if isinstance(word, str):
                            if word not in self.idf_values.keys():
                                counter = 0
                                for one_text in self.corpus:
                                    if one_text:
                                        if word in one_text:
                                            counter += 1
                                self.idf_values[word] = math.log(4 / counter)

    def calculate(self):
        if self.tf_values and self.idf_values:
            for tf_dict in self.tf_values:
                current_dict_of_tf_idf = {}
                for word, tf in tf_dict.items():
                    if self.idf_values[word]:
                        current_dict_of_tf_idf[word] = tf * self.idf_values[word]
                    else:
                        current_dict_of_tf_idf[word] = 0
                self.tf_idf_values.append(current_dict_of_tf_idf)

    def report_on(self, word, document_index):
        result = None
        if self.tf_idf_values:
            if document_index <= len(self.tf_idf_values):
                if isinstance(self.tf_idf_values[document_index], dict):
                    if word in self.tf_idf_values[document_index].keys():
                        value_of_tf_idf = self.tf_idf_values[document_index][word]
                        rating_of_tf_idf = {}
                        tf_idf = set(self.tf_idf_values[document_index].values())
                        tf_idf = sorted(list(tf_idf))
                        print(tf_idf)
                        counter = -1
                        for value in tf_idf:
                            counter += 1
                            rating_of_tf_idf[value] = len(tf_idf) - counter
                        place = rating_of_tf_idf[value_of_tf_idf]
                        result = value_of_tf_idf, place
                    return result


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
