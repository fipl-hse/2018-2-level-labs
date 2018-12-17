import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts):
    list_of_not_words = [
        '!', '@', '#', '$', '%', '^',
        '&', '*', '(', ')', '-', '_',
        '=', '+', '{', '}', '[', ']',
        ',', '.', '/', "'", '"', '<',
        '>', '~', '1', '2', '3', '4',
        '5', '6', '7', '8', '9', '0',
        '\n'
    ]
    if texts is not None:
        clean_list = []
        for sent in texts:
            if isinstance(sent, str) and sent is not None:
                sent = sent.lower()
                sent = sent.replace('<br />', ' ')
                new_sents = ''
                for symbol in sent:
                    if symbol not in list_of_not_words:
                        new_sents += symbol
                new_sents_split = new_sents.split(' ')
                for symb_word in new_sents_split:
                    if symb_word == '':
                        new_sents_split.remove(symb_word)
                clean_list.append(new_sents_split)
        return clean_list
    else:
        return []


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
