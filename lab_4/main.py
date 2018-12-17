import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts):
    if not isinstance(texts, list) or texts == None:
        return []
    words = list()
    list_of_marks = [
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
            new_text = ''
            sentences = list()
            extra_element = '<br />'
            text = text.replce(extra_element, ' ')
            for element in text:
                try:
                    for e in element:
                        if e not in list_of_marks:
                            try:
                                new_text += e
                                continue
                            except IndexError:
                                pass
                        if e in list_of_marks:
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
        self.tf_values = list() #list of dicts
        self.idf_values = dict()
        self.tf_idf_values = list()

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return []
        else:
            for text in self.corpus:
                if not isinstance(text, list):
                    continue
                dict_of_tf = dict()
                len_of_corp = len(text)
                for word in text:
                    if type(word) != str:
                        len_of_corp -= 1
                for word in text:
                    if not isinstance(word, str):
                        continue
                    freq = 0
                    for word2 in text:
                        if word2 == word:
                            freq += 1
                        else:
                            continue
                    tf_of_word = freq / len_of_corp
                    dict_of_tf[word] = tf_of_word
                self.tf_values.append(dict_of_tf)

    def calculate_idf(self):
        if self.corpus == None:
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
                idf_of_word = math.log(num_of_texts / num_of_word)
                self.idf_values[word] = idf_of_word
        

    def calculate(self):
        pass

    def report_on(self, word, document_index):
        pass
