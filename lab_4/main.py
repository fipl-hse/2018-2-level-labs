import math

undesired = list("1234567890/?<>,.()-+=&*^:;%$#@!'""")
REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())

def clean_tokenize_corpus(REFERENCE_TEXTS ) -> list:
    corpus = []
    if REFERENCE_TEXTS is None:
        corpus = []
    else:
        REFERENCE_TEXTS = list(filter(lambda x: x is not None and type(x) == str, REFERENCE_TEXTS))
        if REFERENCE_TEXTS == []:
            corpus = []
        else:
            for el in REFERENCE_TEXTS:
                if "\n" in el:
                    el = el.replace("\n", " ")
                if "<br />" in el:
                    el = el.replace("<br />", " ")
                while "  " in el:
                    el = el.replace("  ", " ")
                el = list(el)
                el = list(filter(lambda x: x not in undesired, el))
                for i in range(len(el)):
                    el[i] = el[i].lower()
                el = ''.join(el)
                el = el.split(" ")
                corpus.append(el)
                for i in range(len(corpus)):
                    corpus[i] = list(filter(lambda x: x != '', corpus[i]))
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
