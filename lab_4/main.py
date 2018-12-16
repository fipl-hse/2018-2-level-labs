import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts):
    words = list()
    list_of_marks = [
         '.', ',', ':', '"', '`', '[', ']',
         '?', '!', '@', '&', "'", '-', '/',
         '$', '^', '*', '(', ')', '=',
         '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
    ]
    for text in texts:
        if isinstance(text, str):
            continue
        new_text = ''
        sentences = list()
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
        pass

    def calculate_tf(self):
        pass

    def calculate_idf(self):
        pass

    def calculate(self):
        pass

    def report_on(self, word, document_index):
        pass
