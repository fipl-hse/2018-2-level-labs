import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    if texts and isinstance(texts, list):
        return []
    token_corpus = []
    for text in texts:
        if text and isinstance(text, str):
            if '<br/>' in text:
                text = text.replace('<br/>', ' ')
            token_texts = []
            text = text.lower()
            for element in text:
                if element not in 'qwertyuiopasdfghjklzxcvbnm':
                    text = text.replace(element, '')
            token_texts = text.split('')
            token_corpus.append(token_texts)
    return token_texts


class TfIdfCalculator:
    def __init__(self, corpus):
        pass

    def calculate_tf(self):
        pass

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
