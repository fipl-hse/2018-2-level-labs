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
    marks = [
        '.', ',', ':', '"', '`', '[', ']',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')', '=',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
        ]
    words = []
    for text in texts:
        if not isinstance(text, str):
            continue
        else:
            not_needed = '<br />'
            text = text.replace(not_needed, ' ')
            new_text = ''
            sentences = []
            for element in text:
                try:
                    for e in element:
                        if e not in marks:
                            try:
                                new_text += e
                                continue
                            except IndexError:
                                pass
                        if e in marks:
                            continue
                except IndexError:
                    pass
            new_text = new_text.lower()
            sentences.append(new_text)
            for sentence in sentences:
                split = sentence.split()
                words.append(split)
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
            new_text = []
            for element in text:
                if isinstance(element, str):
                    new_text.append(element)
            for word in new_text:
                tf_value = new_text.count(word)
                tf_dict[word] = tf_value / len(new_text)
            self.tf_values.append(tf_dict)

    def calculate_idf(self):
        if self.corpus is None:
            return {}
        num_of_texts = len(self.corpus)
        for text in self.corpus:
            if type(text) != list:
                num_of_texts -= 1
        for text in self.corpus:
            if not isinstance(text, list):
                continue
            for word in text:
                if not isinstance(word, str):
                    continue
                num_of_word = 0
                for text2 in self.corpus:
                    if not isinstance(text2, list):
                        continue
                    if word in text2:
                        num_of_word += 1
                self.idf_values[word] = math.log(num_of_texts / num_of_word)

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
