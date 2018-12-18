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
    v_list = []
    for i in texts:
        if not isinstance(i, str):
            continue
        text = ''
        punct = ['.', ',', '!', '?']
        for index in range(0, len(i) - 1):
            if i[index].isalpha():
                text += i[index].lower()
            if i[index] in punct:
                if i[index - 1].isalpha() and i[index + 1].isalpha():
                    continue
            if i[index] is ' ' or "'":
                text += i[index]
                if i[index - 1].isalpha() and i[index + 1] is ' ':
                    text += ' '
            if i[index] in '/':
                if i[index - 1].isalpha() and i[index + 1].isalpha():
                    text += ' '
            if i[index] is '"' or '<' or '>':
                if i[index - 1].isalpha() and i[index + 1].isalpha():
                    continue
                else:
                    text += ' '
        n_text = text.split()
        result = []
        for j in n_text:
            if j == 'br' or 'n':
                continue
            else:
                result.append(j)
        v_list.append(result)
    return v_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.file = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
        self.tf_idf_values = []

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return []
        for i in self.corpus:
            if not isinstance(i, list):
                continue
            dict_tf = {}
            n_i_text = []
            for n_i in i:
                if isinstance(n_i, str):
                    n_i_text.append(n_i)
            for i_word in n_i_text:
                value_tf = n_i_text.count(i_word)
                dict_tf[i_word] = value_tf / len(n_i_text)
            self.tf_values.append(dict_tf)

    def calculate_idf(self):
        if self.corpus is None:
            return {}
        n_list = []
        for f_i in self.corpus:
            n_list.append(f_i)
        words = []
        for s_i in n_list:
            for word in s_i:
                if isinstance(word, str):
                    words.append(word)
        for word in words:
            freq = 0
            if word in self.idf_values:
                continue
            for t_i in n_list:
                if word in t_i:
                    freq += 1
                    continue
            self.idf_values[word] = math.log(len(n_list) / freq)

    def calculate(self):
        if self.idf_values == {} or self.idf_values == None or self.tf_values == [] or self.tf_values == None:
            return []
        for dict_tf in self.tf_values:
            tf_idf = {}
            for word in dict_tf:
                tf_idf[word] = self.idf_values[word] * dict_tf[word]
            self.tf_idf_values.append(tf_idf)

    def report_on(self, word, document_index):
        if self.tf_idf_values == [] or self.tf_idf_values is None:
            return ()
        if document_index > len(self.corpus) - 1:
            return ()
        mid_res= []
        for key, value in self.tf_idf_values[document_index].items():
            mid_res.append((value, key))
        mid_res.sort(reverse=True)
        count = -1
        for i in mid_res:
            count += 1
            if i[1] == word:
                return i[0], count

    def dump_report_csv(self):
        file = open('report.csv', 'w')
        line = 'word,'
        for i in self.file:
            line += 'tf_' + i + ','
        line += 'idf,'
        for i in self.file:
            line += 'tf_idf_' + i + ','
        file.write(i + '\n')
        len = len(self.corpus)
        count = 0
        while len:
            len -= 1
            for word in self.tf_values[count]:
                line = ''
                line += word + ','
                for i in self.tf_values:
                    if word in i:
                        line += str(i[word]) + ','
                        continue
                    else:
                        line += '0,'
                for j in self.idf_values:
                    if word == j:
                        line += str(self.idf_values[word]) + ','
                        break
                for k in self.tf_idf_values:
                    if word in k:
                        line += str(k[word]) + ','
                        continue
                    else:
                        line += '0,'
                file.write(line + '\n')
            count += 1
        file.close()
