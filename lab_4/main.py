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
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        try:
            corpus1 = self.corpus.copy()
            self.corpus = []
            for i in corpus1:
                if type(i) == list:
                    self.corpus.append(i)

            corpus2 = self.corpus.copy()
            self.corpus = []
            for i in corpus2:
                c = i.copy()
                i = []
                for k in c:
                    if type(k) == str:
                        i.append(k)
                self.corpus.append(i)

            res = []
            for text in self.corpus:
                dct = {}
                nk = len(text)
                for w in text:
                    if w in dct.keys():
                        k = dct[w]
                        dct[w] = k + 1
                    else:
                        dct[w] = 1
                for w, nt in dct.items():
                    tf = nt / nk
                    dct[w] = tf
                res.append(dct)
            self.tf_values = res
            return res
        except AttributeError:
            return []

    def calculate_idf(self):
        try:
            corpus1 = self.corpus.copy()
            self.corpus = []
            for i in corpus1:
                if type(i) == list:
                    self.corpus.append(i)

            corpus2 = self.corpus.copy()
            self.corpus = []
            for i in corpus2:
                c = i.copy()
                i = []
                for k in c:
                    if type(k) == str:
                        i.append(k)
                self.corpus.append(i)
                
            d = len(self.corpus)
            dct = {}
            add = []

            for text in self.corpus:
                for i in text:
                    add.append(i)
            add = set(add)

            for w in add:
                for text in self.corpus:
                    if w in text and w in dct.keys():
                        k = dct[w]
                        dct[w] = k + 1
                    elif w in text:
                        dct[w] = 1

            for k, v in dct.items():
                d1 = d / v
                v = math.log(d1)
                dct[k] = v
            self.idf_values = dct

            return dct
        except AttributeError:
            return {}


    def calculate(self):
        try:
            for i in self.tf_values:
                dct = {}
                for k, v in i.items():
                    tf = v
                    idf = self.idf_values.get(k)
                    tf_idf = tf * idf
                    dct[k] = tf_idf
                self.tf_idf_values.append(dct)
            return self.tf_idf_values
        except TypeError:
            return []

    def report_on(self, word, document_index):
        try:
            dct = self.tf_idf_values[document_index]
            org = sorted(dct.items(), key=lambda x: x[1])
            org.reverse()
            print(org)
            for i in org:
                for w in i:
                    if w == word:
                        n = org.index(i)
                        res = (i[1], n)

            return res
        except IndexError:
            return ()
        except TypeError:
            return ()


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
