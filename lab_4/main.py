import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    pass


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        try:
            for text in self.corpus:
                only_words_from_text = []
                tf_one_text = {}
                try:
                    for word in text:
                        if isinstance(word, str) is True:
                            only_words_from_text.append(word)
                    for new_word in only_words_from_text:
                        term_frequency = only_words_from_text.count(new_word) / len(only_words_from_text)
                        tf_one_text[new_word] = term_frequency
                    self.tf_values.append(tf_one_text)
                except TypeError:
                    continue
        except TypeError:
            pass
        return self.tf_values

    def calculate_idf(self):
        pass

    def calculate(self):
        pass

    def report_on(self, word, document_index):
        pass


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
