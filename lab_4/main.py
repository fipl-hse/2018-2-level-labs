import math


REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    list_of_marks = [
        '!', '?', '.', ',', ':', '"', '`', '[', ']', '@', '&', "'", '-',
        '$', '^', '*', '(', ')', '=',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'
    ]

    new_list = []
    if texts is None:
        return new_list
    for sentence in texts:
        if sentence == str(sentence) and sentence is not None:
            new_text = ''
            sentence = sentence.lower()
            sentence = sentence.replace('<br /><br />', ' ')
            for element in sentence:
                if element not in list_of_marks:
                    new_text += element
            new_text = new_text.lower()
            splitted_text = new_text.split(' ')
            for word in splitted_text:
                if word == '' or word == 'br':
                    splitted_text.remove(word)
                print(splitted_text)
            new_list.append(splitted_text)
    return new_list



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


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
