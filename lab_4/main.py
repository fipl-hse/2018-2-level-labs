import math
import string

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    if texts is None or not isinstance(texts, list):
        return []

    punctuation = '"#$%&\'()*+,-/:;<=>@[\\]^_`{|}~!.?'
    new_list = []
    splited_text = []
    for text in texts:
        if isinstance(text, str) and not text is None:
            text = text.replace('<br />', ' ')
            text = text.lower()
            splited_text = text.translate(str.maketrans('', '', punctuation)).split()
            new_list.append(splited_text)
    return new_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus is not None or isinstance(self.corpus, list):
            for line in self.corpus:
                cur_dict = {}
                sum = 0
                len = 0
                if isinstance(line, list) and line is not None and line != []:
                    for word in line:
                        if isinstance(word, str):
                            len += 1
                    for word in line:
                        if isinstance(word, str):
                            for _word in line:
                                if word is _word:
                                    sum += 1
                            if cur_dict.get(word) is None:
                                cur_dict[word] = sum/len
                        sum = 0
                    self.tf_values.append(cur_dict)

    def calculate_idf(self):
        len = 0
        if self.corpus is not None or isinstance(self.corpus, list):
            for line in self.corpus:
                if isinstance(line, list):
                    len += 1
            for line in self.corpus:
                if isinstance(line, list) and line is not None and line != []:
                    for word in line:
                        if isinstance(word, str) and word is not None:
                            sum = 0
                            if self.idf_values.get(word) is None:
                                for _line in self.corpus:
                                    if isinstance(_line, list) and _line is not None and _line != []:
                                        for _word in _line:
                                            if word is _word:
                                                sum += 1
                                                break
                                self.idf_values[word] = math.log(len/sum)

    def calculate(self):
        if self.tf_values is not None and isinstance(self.tf_values, list) and self.tf_values != []:
            if self.idf_values is not None and isinstance(self.idf_values, dict) and self.idf_values != {}:
                for line in self.tf_values:
                    cur_dict = {}
                    for word in line:
                        if not line.get(word) is None and not self.idf_values.get(word) is None: 
                            cur_dict[word] = line.get(word)*self.idf_values.get(word)
                    self.tf_idf_values.append(cur_dict)

    def report_on(self, word, document_index):
        if self.tf_idf_values is not None and isinstance(self.tf_idf_values, list) and not self.tf_idf_values == []:
            if document_index <= len(self.tf_idf_values):
                value = self.tf_idf_values[document_index].get(word)
                position = 0
                if value is not None:
                    for val in self.tf_idf_values[document_index].values():
                        if value < val:
                            position += 1
                return value, position
        return ()

    
    # scenario to check your work
#test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
#tf_idf = TfIdfCalculator(test_texts)
#tf_idf.calculate_tf()
#tf_idf.calculate_idf()
#tf_idf.calculate()
#print(tf_idf.report_on('good', 0))
#print(tf_idf.report_on('and', 1))
