import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
            
def clean_tokenize_corpus(texts: list) -> list:
    if not isinstance(texts, list):
        return []
    n_list = []
    for el in texts:
        if not isinstance(el, str):
            continue
        ex_text = ''
        for ind in range(0, len(el)-1):
            if el[ind].isalpha():
                ex_text += el[ind].lower()
            if el[ind] is ' ' or el [ind] is "'":
                ex_text += el[ind]
            if el[ind] in ['.', ',', '!', '?']:
                if el[ind-1].isalpha() and el[ind+1].isalpha():
                    continue
                if el[ind-1].isalpha() and el[ind+1] is ' ':
                    ex_text += ' '
            if el[ind] in '/':
                if el[ind-1].isalpha() and el[ind+1].isalpha():
                    ex_text += ' '
            if el[ind] is '"' or el[ind] is '<' or el[ind] is '>':
                if el[ind-1].isalpha() and el[ind+1].isalpha():
                    continue
                else:
                    ex_text += ' '
        n_text = ex_text.split()
        result = []
        for elem in n_text:
            if elem == 'br' or elem == 'n':
                continue
            else:
                result.append(elem)
        n_list.append(result)
    return n_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return []
        for el in self.corpus:
            if not isinstance(el, list):
                continue
            tf_dict = {}
            n_el_text = []
            for n_el in el:
                if isinstance(n_el, str):
                    n_el_text.append(n_el)
            for el_word in n_el_text:
                tf_value = n_el_text.count(el_word)
                tf_dict[el_word] = tf_value / len(n_el_text)
            self.tf_values.append(tf_dict)
            
    def calculate_idf(self):
        if self.corpus is None:
            return {}
        new_list = []
        for el in self.corpus:
            if el:
                new_list.append(el)
        words = []
        for a_el in new_list:
            for word in a_el:
                if isinstance(word, str):
                    words.append(word)
        for word in words:
            w_freq = 0
            if word in self.idf_values:
                continue
            for om_text in new_list:
                if word in om_text:
                    w_freq += 1
                    continue
            self.idf_values[word] = math.log(len(new_list) / w_freq)
            
    def calculate(self):
        if self.idf_values == {} or self.tf_values == [] or self.tf_values is None or self.idf_values is None:
            return []
        for tf_dict in self.tf_values:
            tf_idf = {}
            for word in tf_dict:
                tf_idf[word] = tf_dict[word] * self.idf_values[word]
            self.tf_idf_values.append(tf_idf)
            
    def report_on(self, word, document_index):
        if self.tf_idf_values == [] or self.tf_idf_values is None:
            return ()
        if document_index > len(self.corpus)-1:
            return ()
        reverse = []
        for key, value in self.tf_idf_values[document_index].items():
            reverse.append((value, key))
        reverse.sort(reverse=True)
        count = -1
        for el in reverse:
            count += 1
            if el[1] == word:
                return el[0], count
            
    def dump_report_csv(self):
        file = open('result.csv', 'w')
        f_line = 'word,'
        for title in self.file:
            f_line += 'tf_'+title+','
        f_line += 'idf,'
        for title in self.file:
            f_line += 'tf_idf_'+title+','
        file.write(f_line+'\n')
        length = len(self.corpus)
        count = 0
        while length:
            length -= 1
            for word in self.tf_values[count]:
                second = ''
                second += word+','
                for el in self.tf_values:
                    if word in el:
                        second += str(el[word])+','
                        continue
                    else:
                        second += '0,'
                for elem in self.idf_values:
                    if word == elem:
                        second += str(self.idf_values[word])+','
                        break
                for element in self.tf_idf_values:
                    if word in element:
                        second += str(element[word])+','
                        continue
                    else:
                        second += '0,'
                file.write(second+'\n')
            count += 1
        file.close()
