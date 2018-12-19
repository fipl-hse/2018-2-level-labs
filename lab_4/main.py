import math
import csv

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
           return []
        else:
            for i in range(len(self.tf_values)):
                dic = {}
                for k,v in self.tf_values[i].items():
                    dic[k] = v * self.idf_values[k]
                self.tf_idf_values.append(dic)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if self.tf_idf_values is None:
            return ()
        elif self.tf_idf_values is []:
            return ()
        elif document_index >= len(self.tf_idf_values):
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

    def dump_report_csv(self):
        table = []
        flst = ['TF_values_' + text for text in texts]
        flst1 = ['TF_IDF_values_' + text for text in texts]
        flst.insert(0, 'word')
        flst1.insert(0, 'IDF_values')
        table_head = flst + flst1
        table.append(table_head)
        for word in self.idf_values.keys():
            TFs = []
            TF_IDFs = []
            for i in range(len(self.tf_values)):
                if word in self.tf_values[i].keys():
                    TFs.append(str(self.tf_values[i][word]))
                else:
                    TFs.append('0')
            for i in range(len(self.tf_idf_values)):
                if word in self.tf_idf_values[i].keys():
                    TF_IDFs.append(str(self.tf_idf_values[i][word]))
                else:
                    TF_IDFs.append('0')
            TFs.insert(0, word)
            TF_IDFs.insert(0, (str(self.idf_values[word])))
            line = TFs + TF_IDFs
            table.append(line)
        with open('report.csv', "w", newline='') as csv_file:
             writer = csv.writer(csv_file, delimiter=',')
             for line in table:
                 writer.writerow(line)

    def cosine_distance(self, index_text_1, index_text_2):
        all_words = []
        for k in self.tf_idf_values[index_text_1].keys():
            if k not in all_words:
                all_words.append(k)
        for k in self.tf_idf_values[index_text_2].keys():
            if k not in all_words:
                all_words.append(k)
        vec1 = []
        vec2 = []
        for word in all_words:
            if word in self.tf_idf_values[index_text_1].keys():
                vec1.append(self.tf_idf_values[index_text_1][word])
            else:
                vec1.append(0)
            if word in self.tf_idf_values[index_text_2].keys():
                vec2.append(self.tf_idf_values[index_text_2][word])
            else:
                vec2.append(0)
        nom = 0
        underroot1 = 0
        underroot2 = 0
        for i in range(len(vec1)):
            nom += vec1[i] * vec2[i]
            underroot1 += vec1[i] ** 2
            underroot2 += vec2[i] ** 2
        denom = math.sqrt(underroot1) + math.sqrt(underroot2)
        return nom / denom

# scenario to check your work
corpus = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(corpus)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
