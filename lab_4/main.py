import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(REFERENCE_TEXTS) -> list:
    corpus = []
    for c in REFERENCE_TEXTS:
        if "\n" in c:
            c = c.replace("\n", " ")
        if "<br />" in c:
            c = c.replace("<br />", " ")
        while "  " in c:
            c = c.replace("  ", " ")
        c = list(c)
        c = list(filter(lambda x: x not in undesired, c))
        for i in range(len(c)):
            c[i] = c[i].lower()
        c = ''.join(c)
        c = c.split(" ")
        corpus.append(c)
    return corpus


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
