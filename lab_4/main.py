import math

undesired = list("1234567890/?<>,.()-+=&*^:;%$#@!'""")
REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(REFERENCE_TEXTS) -> list:
    corpus = []
    if REFERENCE_TEXTS is None:
       corpus = []
    else:
       REFERENCE_TEXTS = list(filter(lambda x: x is not None and type(x) == str, REFERENCE_TEXTS))
       if REFERENCE_TEXTS == []:
          corpus = []
       else:
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
            for text in self.corpus:
                text = list(filter(lambda x: type(x) == str, text))
                dic = {}
                for i in range(len(text)):
                    num = 0
                    for c in text:
                        if text[i] == c:
                            num += 1
                    dic[text[i]] = num / len(text)
                self.tf_values.append(dic)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus is None:
            self.tf_values = []
        else:
            all_words = []
            self.corpus = list(filter(lambda x: x is not None and type(x) == list, self.corpus))
            for i in range(len(self.corpus)):
                self.corpus[i] = list(filter(lambda x: type(x) == str, self.corpus[i]))
                for word in self.corpus[i]:
                    if word not in all_words:
                        all_words.append(word)
                for word in all_words:
                    num = 0
                    for i in range(len(self.corpus)):
                        if word in self.corpus[i]:
                            num += 1
                    self.idf_values[word] = math.log(len(self.corpus) / num)
        return self.idf_values

    def calculate(self):
        if self.tf_values == [] or self.idf_values == {} or self.tf_values is None or self.idf_values is None:
            self.tf_idf_values = []
        else:
            for i in range(len(self.tf_values)):
                dic = {}
                for k,v in self.tf_values[i].items():
                    dic[k] = v * self.idf_values[k]
                self.tf_idf_values.append(dic)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if document_index >= len(self.tf_idf_values) or self.tf_idf_values == [] or self.tf_idf_values is None:
            return ()
        else:
            val = []
            for v in self.tf_idf_values[document_index].values():
                if v not in val:
                    val.append(v)
            ord_list = []
            while len(val) != 0:
                maxi = max(val)
                ord_list.append(maxi)
                val.remove(maxi)
            return (self.tf_idf_values[document_index][word], ord_list.index(self.tf_idf_values[document_index][word]))

        print(report_on('this', 0))

# scenario to check your work
#corpus = clean_tokenize_corpus(REFERENCE_TEXTS)
#tf_idf = TfIdfCalculator(corpus)
#tf_idf.calculate_tf()
#tf_idf.calculate_idf()
#tf_idf.calculate()
#print(tf_idf.report_on('good', 0))
#print(tf_idf.report_on('and', 1))
