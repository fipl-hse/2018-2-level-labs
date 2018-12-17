import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    clean_corpus = []
    if texts  and isinstance(texts,list):
        for one_text in texts:
            if one_text and isinstance(one_text, str):
                while '<br />' in one_text:
                    one_text = one_text.replace('<br />', ' ')
                clean_texts = []
                words = one_text.split(' ')
                for word in words:
                    word = word.lower()
                    new_word = ''
                    if not word.isalpha():
                        for index in word:
                            if index.isalpha():
                                new_word += index
                        if new_word:
                            clean_texts.append(new_word.lower())
                    else:
                        clean_texts.append(word.lower())
                clean_corpus += [clean_texts]
        return clean_corpus
    else:
        return clean_corpus



class TfIdfCalculator:
    def __init__(self, corpus):
        self.tf_values = []
        self.corpus = corpus
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if isinstance(self.corpus,list):
            for one_text in self.corpus:
                if not isinstance(one_text, list):
                    continue
                dict_tf = {}
                new_word_text = []
                for word in one_text:
                    if isinstance(word, str):
                        new_word_text.append(word)
                for new_word in new_word_text:
                    tf_value = new_word_text.count(new_word)
                    dict_tf[new_word] = tf_value / len(new_word_text)
                self.tf_values.append(dict_tf)
        else:
            return []





    def calculate_idf(self):
        new_list_text = []
        if isinstance(self.corpus,list):
            for one_text in self.corpus:
                if one_text:
                    new_list_text.append(one_text)
                #texts_number = len(new_list_text)
            new_word_text = []
            for element in new_list_text:
                for word in element:
                    if isinstance(word, str):
                        new_word_text.append(word)
            for new_word in new_word_text:
                freq_word = 0
                if new_word in self.idf_values:
                    continue
                for text_try in new_list_text:
                    if new_word in text_try:
                        freq_word += 1
                        continue
                self.idf_values[new_word] = math.log(len(new_list_text)/freq_word)
            return self.idf_values
        else:
            return []



    def calculate(self):
        if self.idf_values and self.tf_values:

            for values in self.tf_values:
                tf_idf_values = {}
                for word in values:
                    tf_idf_values[word] = values[word] * self.idf_values[word]
                self.tf_idf_values.append(tf_idf_values)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        # if document_index < len(self.tf_idf_values) and self.tf_idf_values:
        reversed_list = []
        tf_idf_dict = self.tf_idf_values[document_index]
        for freq, value in tf_idf_dict.items():
            reversed_list.append((value, freq))
        reversed_list.sort(reverse=True)
        counter = -1
        for element in reversed_list:
            counter += 1
            if element[1] == word:
                return element[0], counter

# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
