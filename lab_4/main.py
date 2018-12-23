import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    if not isinstance(texts, list) or not texts:
        return []
    words = []
    marks = [
        '.', ',', ':', '"', '`', '[', ']',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')', '=',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
    ]
    
    for text in texts:
        if not isinstance(text, str):
            continue
        else:
            clean_text = ''
            extra = '<br />'
            sentences = []
            for i in text:
                try:
                    for e in i:
                        if e not in marks:
                            try:
                                clean_text += e
                                continue
                            except IndexError:
                                pass
                        if e in marks:
                            continue
                except IndexError:
                    pass
                
            clean_text = clean_text.lower()
            sentences.append(new_text)
            
            for sentence in sentences:
                splitted = sentence.split()
                words.append(splitted)
    return words


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return []
        for text in self.corpus:
            if not isinstance(text, list):
                continue
            tf_dict = {}
            
            corpus_len = len(text)
            for i in text:
                if type(i) != str:
                corpus_len -= 1
            for i in text:
                if not isinstance(i, str):
                    continue
                frequency = 0
                for e in text:
                    if e == i:
                        frequency += 1
                    else:
                        continue
                tf_of_word = frequency / corpus_len
                dict_of_tf[i] = tf_of_word
            self.tf_values.append(dict_of_tf)

    def calculate_idf(self):
        if self.corpus is None:
            return {}
        texts_len = len(self.corpus)
        for text in self.corpus:
            if type(text) != list:
                texts_len -= 1
        for text in self.corpus:
            if not isinstance(text, list):
                continue
            for i in text:
                if not isinstance(i, str):
                    continue
                word_quant = 0
                for another_text in self.corpus:
                    if not isinstance(another_text, list):
                        continue
                    if i in another_text:
                        word_quant += 1
                self.idf_values[i] = math.log(texts_len / word_quant)

    def calculate(self):
        if self.tf_values is None or self.idf_values is None:
            return []
        if self.idf_values == {} or self.tf_values == []:
            return []
        for tf_dict in self.tf_values:
            tf_idf = {}
            for word in tf_dict:
                tf_idf[word] = tf_dict[word] * self.idf_values[word]
            self.tf_idf_values.append(tf_idf)

    def report_on(self, word, document_index):
        if document_index > len(self.corpus) - 1:
            return ()
        if self.tf_idf_values == [] or self.tf_idf_values is None:
            return ()
        report_on_word = []
        text = self.corpus[document_index]
        dict_tf_idf = self.tf_idf_values[document_index]
        lst = list()
        for token in text:
            if token in dict_tf_idf:
                lst.append((dict_tf_idf[token], token))
        lst.sort(reverse=True)
        for element in lst:
            if word == element[1]:
                tf_idf_value = element[0]
                position = lst.index(element)
                report_on_word.append((tf_idf_value, position))
        return report_on_word[0]


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
