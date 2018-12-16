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
    counter = 0
    word = ''

    if isinstance(texts,list) == False:
        return []
    for part in texts:
        if isinstance(part,str) == True:
            counter += 1
            part = part.lower()
            for element in part:
                if element == '<':
                        new_part = part[part.find(element):]
                        neces_part1 = part[:part.find(element)]
                        for el in new_part:
                            if el == '>':
                                neces_part2 = new_part[1 + new_part.find(el):]
                                res_part = neces_part1 + neces_part2
                                part = res_part

                                
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
        

    if counter == 0:
        return []

    return final_list

from fractions import Fraction
class TfIdfCalculator:
    corpus = []
    tf_values = []
    tf_values_num = []
    idf_values = []
    tf_idf_values = []
    
    def __init__(self, corpus):
        self.corpus = corpus

    def calculate_tf(self):
        vocub = {}
        final_vocub = {}
        final_vocub_num = {}
        number_of_words_in_voc = 0
        if isinstance(self.corpus,list): 
            for part in self.corpus:
                for word in part:
                    number_of_words_in_voc += 1
                    if word in vocub:
                        vocub[word]+=1
                    else:
                        vocub.update({word:1})
                for key,value in vocub.items():
                    tf_value_num = value/number_of_words_in_voc
                    tf_value = str(value) + ' / ' + str(number_of_words_in_voc)
                    final_vocub[key] = tf_value
                    final_vocub_num[key] = tf_value_num


                self.tf_values.append(final_vocub)
                self.tf_values_num.append(final_vocub_num)
                vocub = {}
                final_vocub = {}
                number_of_words_in_voc = 0



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
