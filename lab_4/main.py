import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:  
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sent_list = []
    final_list = []
    Flag = 0
    word = ''

    if isinstance(texts,list) == False:
        return []
    for part in texts:
        if isinstance(part,str) == True:
            Flag += 1

            part = part.lower()
            for element in part:
                if element in alph:
                    word += element

                else:
                    if element == ' ' and word != '' or element == '.':
                        sent_list.append(word)
                        word = ''
            
        if sent_list != []:
            final_list.append(sent_list)
            sent_list = []

    if Flag == 0:
        return []
        print('flag был 0')

    return final_list


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
