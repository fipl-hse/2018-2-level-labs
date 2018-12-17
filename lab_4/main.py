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
        garbage = '<br />'
        spam = '''' " @ $ % ^ & * ( ) _ = + , / { [ } ] ; : < > ' / # . ! ? \n'''
        spam = spam.split(' ')
        spam.append('-')
        trash = '  '
        texts1 = texts.copy()
        texts = []

        for i in texts1:
            if type(i) == str:
                texts.append(i)

        for text in texts:
            if garbage in text:
                text = text.replace(garbage, ' ')
            for i in spam:
                if i in text:
                    text = text.replace(i, '')
            if trash in text:
                text = text.replace(trash, ' ')
            res1.append(text)
        print(res1)

        for i in res1:
            res2 = []
            for k in i:
                if k.isupper():
                    s = k.lower()
                    i = i.replace(k, s)
            res2.append(i)
            for l in res2:
                l = l.split(' ')
                res.append(l)

        return res

    except AttributeError:
        return []


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
