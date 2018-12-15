import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    TEXTS = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in TEXTS:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts_corpus: list) -> list:
    if not texts_corpus or not isinstance(texts_corpus, list):
        return []
    clean_token_corpus = []
    for one_text in texts_corpus:
        if one_text and isinstance(one_text, str):
            while '<br />' in one_text:
                one_text = one_text.replace("<br />", " ")
            clean_token_text = []
            words = one_text.split(" ")
            for index, word in enumerate(words):
                new_word = ""
                if not word.isalpha():
                    for i in word.lower():
                        if i.isalpha():
                            new_word += i
                    if new_word:
                        clean_token_text.append(new_word.lower())
                else:
                    clean_token_text.append(word.lower())
            clean_token_corpus += [clean_token_text]
    return clean_token_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if self.corpus:
            for part in self.corpus:
                tf_values = {}
                if part:
                    len_text = len(part)
                    for word in part:
                        if not isinstance(word, str):
                            len_text -= 1
                    for word in part:
                        if isinstance(word, str) and word not in tf_values:
                            count_word = part.count(word)
                            tf_values[word] = count_word / len_text
                    self.tf_values += [tf_values]
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            for part in self.corpus:
                if not part:
                    continue
                new_corpus = []
                for word in part:
                    if word not in new_corpus and isinstance(word, str):
                        new_corpus += [word]
                count_words = {}
                for word in new_corpus:
                    count_word = 0
                    for text_again in self.corpus:
                        if not text_again or word in text_again:
                            count_word += 1
                    count_words[word] = count_word
                    if count_words.get(word) != 0:
                        len_c = len(self.corpus)
                        self.idf_values[word] = math.log(len_c / count_words.get(word))
            return self.idf_values

    def calculate(self):
        if self.idf_values and self.tf_values:
            for part in self.tf_values:
                tf_idf_values = {}
                for word, tf_value in part.items():
                    tf_idf_values[word] = tf_value * self.idf_values.get(word)
                self.tf_idf_values += [tf_idf_values]
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf_dict = self.tf_idf_values[document_index]
        if not word in tf_idf_dict:
            return ()
        list_tf_idf = sorted(tf_idf_dict, key=tf_idf_dict.__getitem__, reverse=True)
        return tf_idf_dict.get(word.lower()), list_tf_idf.index(word.lower())

    def dump_report_csv(self):
        with open("report.csv", "w", encoding="utf-8") as report:
            tf_str = ""
            tf_idf_str = ""
            for i in self.file_names:
                tf_str += "tf_" + i + ","
                tf_idf_str += "tf_idf_" + i + ","
            first_line = "word," + tf_str + "idf," + tf_str[:-1]
            table = [first_line]
            dict_report = {}
            for index, text_dict in enumerate(self.tf_values):
                if text_dict:
                    for word, tf_value in text_dict.items():
                        idf = self.idf_values.get(word)
                        tf_idf = tf_value * idf
                        dict_report[word+str(index)] = str(tf_value) + ','
                        dict_report[word+str(index)] += str(idf) + ","
                        dict_report[word+str(index)] += str(tf_idf)
            report_text = ["–" for i in range(len(self.corpus) * 2 + 2)]
            reports = []
            whole_report = sorted(dict_report.items())
            list_words = []
            for one_part in whole_report:
                word_with_index = one_part[0]
                value = one_part[1]
                values = value.split(',')
                word = word_with_index[:-1]
                if word not in list_words:
                    report_text = ["–" for i in range(len(self.corpus) * 2 + 2)]
                index = int(word_with_index[-1])
                report_text[0] = word
                report_text[index+1] = values[0]
                report_text[len(self.corpus) + 1] = values[1]
                report_text[len(self.corpus) + index + 2] = values[2]
                if word in list_words:
                    reports[-1] = report_text
                else:
                    reports.append(report_text)
                list_words += [word]
            for i in reports:
                new_line = ",".join(i)
                table += [new_line]
            result = "\n".join(table)
            report.write(result)

    def cosine_distance(self, index_text_1, index_text_2):
        if index_text_1 >= len(self.corpus) or index_text_2 >= len(self.corpus):
            return 100000000000
        new_words = []
        text_1 = self.corpus[index_text_1]
        text_2 = self.corpus[index_text_2]
        for word in text_1:
            if word not in new_words:
                new_words += [word]
        for word in text_2:
            if word not in new_words:
                new_words.append(word)

        vector_1 = [[] for i in range(len(new_words))]
        vector_2 = [[] for i in range(len(new_words))]

        tf_idf_values = {}
        for part in self.tf_idf_values:
            tf_idf_values.update(part)

        for index, word in enumerate(new_words):
            if word in text_1:
                vector_1[index] = tf_idf_values.get(word)
            elif word not in text_1:
                vector_1[index] = 0
            if word in text_2:
                vector_2[index] = tf_idf_values.get(word)
            elif word not in text_2:
                vector_2[index] = 0

        numerators = [vector_1[i] * vector_2[i] for i in range(len(vector_1))]
        numerator = sum(numerators)
        denominators_1 = [j**2 for j in vector_1]
        denominators_2 = [j**2 for j in vector_2]
        denominator = math.sqrt(sum(denominators_1)) * math.sqrt(sum(denominators_2))
        cos_vectors = numerator / denominator
        return cos_vectors
