import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    try:
        res = []
        res1 = []
        spam =['<br />']
        spam1 = '''' " @ $ % ^ & * ( ) _ - = + , / { [ } ] ; : < > ' / # . ! ? \n'''
        spam1 = spam1.split(' ')
        spam = spam+spam1
        spam.append('  ')

        texts1 = texts.copy()
        texts = []

        for i in texts1:
            if type(i) == str:
                texts.append(i)

        for text in texts:
            for i in spam:
                if i in text:
                    text = text.replace(i, '')
                if i.isupper():
                    text = text.replace(i, i.lower())
            res1.append(text)

        for i in res1:
            res2 = i.split(' ')
            res.append(res2)

    except AttributeError:
        return []

    return res


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
