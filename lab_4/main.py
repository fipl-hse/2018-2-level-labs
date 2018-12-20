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
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus is None:
            self.tf_values = []
        else:
            self.corpus = list(filter(lambda x: x is not None and type(x) == list, self.corpus))
            for item in self.corpus:
                item = list(filter(lambda x: type(x) == str, item))
                dic = {}
                for i in range(len(item)):
                    counter = 0
                    for el in item:
                        if item[i] == el:
                            counter += 1
                    dic[item[i]] = counter / len(item)
                self.tf_values.append(dic)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus is None:
            self.tf_values = []
        else:
            words_storage = []
            self.corpus = list(filter(lambda x: x is not None and type(x) == list, self.corpus))
            for i in range(len(self.corpus)):
                self.corpus[i] = list(filter(lambda x: type(x) == str, self.corpus[i]))
                for word in self.corpus[i]:
                    if word not in words_storage:
                        words_storage.append(word)
                for word in words_storage:
                    counter = 0
                    for i in range(len(self.corpus)):
                        if word in self.corpus[i]:
                            counter += 1
                    self.idf_values[word] = math.log(len(self.corpus) / counter)
        return self.idf_values

    def calculate(self):
        if self.tf_values == [] or self.idf_values == {} or self.tf_values is None or self.idf_values is None:
            return []
        else:
            for i in range(len(self.tf_values)):
                sl = {}
                for k, v in self.tf_values[i].items():
                    sl[k] = v * self.idf_values[k]
                self.tf_idf_values.append(sl)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if self.tf_idf_values is None:
            return ()
        elif self.tf_idf_values is []:
            return ()
        elif document_index >= len(self.tf_idf_values):
            return ()
        else:
            zn = []
            for v in self.tf_idf_values[document_index].values():
                if v not in zn:
                    zn.append(v)
            ordered = []
            while len(zn) != 0:
                maxi = max(zn)
                ordered.append(maxi)
                zn.remove(maxi)
            return (self.tf_idf_values[document_index][word], ordered.index(self.tf_idf_values[document_index][word]))


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
