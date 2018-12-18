import math
import string

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    improved_corpus = []
    punct = '"#$%&\'()*+,-/:;<=>@[\\]^_`{|}~!.?'
    if type(texts) is not list:
        return[]
    for text in texts:
        if isinstance(text, str) and not text is None:
            text = text.replace('<br />', ' ')
            text = text.lower()
            improved_text = text.translate(str.maketrans('', '', punct)).split()
            improved_corpus.append(improved_text)
    return improved_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if type(self.corpus) is not list:
            return []
        for el in self.corpus:
            if type(el) is not list:
                continue
            tf_dict = {}
            new_el_text = []
            for i in el:
                if type(i) is str:
                    new_el_text.append(i)
            for word in new_el_text:
                tf_value = new_el_text.count(word)
                tf_dict[word] = tf_value / len(new_el_text)
            self.tf_values.append(tf_dict)
    def calculate_idf(self):
        text_list = []
        if self.corpus is None:
            return self.idf_values
        for c_text in self.corpus:
            if c_text:
                text_list.append(c_text)
        words = []
        for element in text_list:
            for word in element:
                if type(word) == str:
                    text_list.append(word)
        for word in words:
            fr = 0
            if word in self.idf_values:
                continue
            for cur_text in text_list:
                if word in cur_text:
                    fr += 1
                    continue
            self.idf_values[word] = math.log(len(list) / fr)



    def calculate(self):
        if self.idf_values and self.tf_values:
            for tf_dict in self.tf_values:
                tf_idf = {}
                for word in tf_dict:
                    tf_idf[word] = tf_dict[word] * self.idf_values[word]
                self.tf_idf_values.append(tf_idf)
            return self.tf_idf_values




    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()

        reversed_list = []
        tf_idf_dict = self.tf_idf_values[document_index]
        for key, value in tf_idf_dict.items():
            reversed_list.append((value, key))
        reversed_list.sort(reverse=True)
        counter = -1
        for el in reversed_list:
            counter += 1
            if el[1] == word:
                return el[0], counter


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
