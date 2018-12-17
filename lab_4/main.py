import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    texts_list = []
    try:
        for text in texts:
            try:
                if '<br />' in text:
                    text = text.replace('<br />', ' ')
                text = text.lower()
                for symbol in text:
                    if symbol not in 'abcdefghijklmnopqrstuvwxyz ':
                        text = text.replace(symbol, '')
                tokens_list = text.split()
                texts_list.append(tokens_list)
            except TypeError:
                continue
            except AttributeError:
                continue
    except TypeError:
        pass
    return texts_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus is None:
            return []
        for text in self.corpus:
            if text is None:
                continue
            only_words_from_text = []
            tf_one_text = {}
            for word in text:
                if isinstance(word, str):
                    only_words_from_text.append(word)
            for new_word in only_words_from_text:
                term_frequency = only_words_from_text.count(new_word) / len(only_words_from_text)
                tf_one_text[new_word] = term_frequency
            self.tf_values.append(tf_one_text)
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
