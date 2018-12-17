import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    if not texts or not isinstance(texts, list):
        return []
    lst_corpus = []
    for text in texts:
        if text and isinstance(text, str):
            while '<br />' in text:
                text = text.replace("<br />", " ")
            lst_text = []
            words = text.split()
            for ind, el in enumerate(words):
                clean_word = ''
                if el.isalpha():
                    lst_text.append(el.lower())
                else:
                    for element in el.lower():
                        if element.isalpha():
                            clean_word += element
                    if clean_word:
                        lst_text.append(clean_word)
            lst_corpus.append(lst_text)
    return lst_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus:
            for text in self.corpus:
                tf = {}
                if text:
                    len_text = len(text)
                    for word in text:
                        if not isinstance(word, str):
                            len_text -= 1
                    for word in text:
                        if isinstance(word, str) and word not in tf:
                            num = text.count(word)
                            tf[word] = num / len_text
                    self.tf_values += [tf]
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            dict_count_texts = {}
            for text in self.corpus:
                if not text:
                    continue
                word_list = []
                for word in text:
                    if word not in word_list and isinstance(word, str):
                        word_list.append(word)
                for element in word_list:
                    count_word_in_corpus = 0
                    for another_text in self.corpus:
                        if not another_text or element in another_text:
                            count_word_in_corpus += 1
                    dict_count_texts[element] = count_word_in_corpus
                    if dict_count_texts.get(element) != 0:
                        length = len(self.corpus)
                        self.idf_values[element] = math.log(length / dict_count_texts.get(element))
            return self.idf_values

    def calculate(self):
        if self.tf_values and self.idf_values:
            for elenent in self.tf_values:
                tf_idf_d = {}
                for word, tf in elenent.items():
                    tf_idf_d[word] = tf * self.idf_values.get(word)
                self.tf_idf_values += [tf_idf_d]
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf_d = self.tf_idf_values[document_index]
        significance = sorted(tf_idf_d, key=tf_idf_d.__getitem__, reverse=True)
        return tf_idf_d.get(word.lower()), significance.index(word.lower())


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
