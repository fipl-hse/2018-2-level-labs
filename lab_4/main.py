import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    pass
    if type(texts) != list:
        return []
    new_l = []
    for element in texts:
        if type(element) != str:
            continue
        txt = ''
        for i in range(0, len(element) - 1):
            if element[i].isalpha():
                txt += element[i].lower()
            if element[i] == ' ' or element[i] == "'":
                txt += element[i]
            if element[i] in ['.', ',', '!', '?']:
                if element[i - 1].isalpha() and element[i + 1].isalpha():
                    continue
                if element[i - 1].isalpha() and element[i + 1] == ' ':
                    txt += ' '
            if element[i] in '/':
                if element[i - 1].isalpha() and element[i + 1].isalpha():
                    txt += ' '
            if element[i] == '"' or element[i] is '<' or element[i] is '>':
                if element[i - 1].isalpha() and element[i + 1].isalpha():
                    continue
                else:
                    txt += ' '
        n_text = txt.split()
        res = []
        for el in n_text:
            if el == 'n' or el == 'br':
                continue
            else:
                res.append(el)
        new_l.append(res)
    return new_l


class TfIdfCalculator:
    def __init__(self, corpus):
        pass
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        #self.file = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        pass
        if type(self.corpus) != list:
            return []
        for elem in self.corpus:
            if type(elem) != list:
                continue
            tf_dictionary = {}
            n_el_txt = []
            for e in elem:
                if isinstance(e, str):
                    n_el_txt.append(e)
            for e_word in n_el_txt:
                tf_value = n_el_txt.count(e_word)
                tf_dictionary[e_word] = tf_value / len(n_el_txt)
            self.tf_values.append(tf_dictionary)



    def calculate_idf(self):
        pass
        if self.corpus == None:
            return {}
        list = []
        for current in self.corpus:
            if current:
                list.append(current)
        full_txt = []
        for full_el in list:
            for word in full_el:
                if type(word) == str:
                    full_txt.append(word)
        for word in full_txt:
            freqency = 0
            if word in self.idf_values:
                continue
            for current_text in list:
                if word in current_text:
                    freqency += 1
                    continue
            self.idf_values[word] = math.log(len(list) / freqency)

    def calculate(self):
        pass

        if self.tf_values and self.idf_values:
            for tf_dictionary in self.tf_values:
                new_dict_idf_tf = {}
                for word, tf in tf_dictionary.items():
                    if self.idf_values[word]:
                        new_dict_idf_tf[word] = tf * self.idf_values[word]
                    else:
                        new_dict_idf_tf[word] = 0
                self.tf_idf_values.append(new_dict_idf_tf)

    def report_on(self, word, document_index):
        pass
        if type(self.tf_idf_values) != list:
            return ()
        if (document_index > len(self.corpus) - 1):
            return ()
        if(len(self.tf_idf_values) == 0):
            return ()
        num = 0
        txt_n = self.corpus[document_index]
        present_tf_idf_dict = self.tf_idf_values[document_index]
        w_tf_idf_list = list()
        if word not in present_tf_idf_dict.keys():
            return ()
        for w_2 in txt_n:
            if w_2 in present_tf_idf_dict:
                w_tf_idf_list.append((present_tf_idf_dict[w_2], w_2))
        w_tf_idf_list.sort(reverse=True)
        for i, b in enumerate(w_tf_idf_list):
            if b[1] == word:
                num = i
                break
        res = (present_tf_idf_dict[word], num)

        return res


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
