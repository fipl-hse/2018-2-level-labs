import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(all_texts: list) -> list:
    if not isinstance(all_texts, list):
        return []
    alphabet_checker = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    new_list_texts = []
    for _text in all_texts:
        if not isinstance(_text, str):
            continue
        current_text = ''
        for index in range(0, len(_text)-1):
            if _text[index] is 'A':
                current_text += _text[index].lower()
                continue
            if _text[index] is ' ':
                current_text += ' '
                continue
            if _text[index] in alphabet_checker:
                current_text += _text[index].lower()
                continue
            if _text[index] in ['.', ',', '!', '?']:
                if _text[index-1] in alphabet_checker and _text[index+1] in alphabet_checker:
                    continue
                if _text[index-1] in alphabet_checker and _text[index+1] is ' ':
                    current_text += ' '
                    continue
            if _text[index] is "'":
                current_text += "'"
            if _text[index] in '/':
                if _text[index-1] in alphabet_checker and _text[index+1] in alphabet_checker:
                    current_text += ' '
                    continue
            if _text[index] is '"':
                if _text[index-1] in alphabet_checker and _text[index+1] in alphabet_checker:
                    continue
                else:
                    current_text += ' '
            if _text[index] is '<' or _text[index] is '>':
                if _text[index-1] in alphabet_checker and _text[index+1] in alphabet_checker:
                    continue
                else:
                    current_text += ' '
                    continue
        new_text = current_text.split()
        res = []
        for element in new_text:
            if element == 'br' or element == 'n':
                continue
            else:
                res.append(element)
        new_list_texts.append(res)
    return new_list_texts


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return []
        for element_text in self.corpus:
            if not isinstance(element_text, list):
                continue
            tf_dict = {}
            new_element_text = []
            for element in element_text:
                if isinstance(element, str):
                    new_element_text.append(element)
            for element_word in new_element_text:
                tf_value = new_element_text.count(element_word)
                tf_dict[element_word] = tf_value / len(new_element_text)
            self.tf_values.append(tf_dict)

    def calculate_idf(self):
        if self.corpus is None:
            return {}
        new_corpus = []
        for b_text in self.corpus:
            if b_text:
                new_corpus.append(b_text)
        all_words = []
        for a_text in new_corpus:
            for word in a_text:
                if isinstance(word, str):
                    all_words.append(word)
        for word in all_words:
            word_freq = 0
            if word in self.idf_values:
                continue
            for c_text in new_corpus:
                if word in c_text:
                    word_freq += 1
                    continue
            self.idf_values[word] = math.log(len(new_corpus) / word_freq)

    def calculate(self):
        if self.idf_values == {} or self.tf_values == []:
            return []
        if self.tf_values is None or self.idf_values is None:
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
        list_reversed = []
        for key, value in self.tf_idf_values[document_index].items():
            list_reversed.append((value, key))
        list_reversed.sort(reverse=True)
        counter = -1
        for element in list_reversed:
            counter += 1
            if element[1] == word:
                return element[0], counter

    def dump_report_csv(self):
        file = open('results.csv', 'w')
        top_line = 'word,'
        for text_title in self.file_names:
            top_line += 'tf_'+text_title+','
        top_line += 'idf,'
        for text_title in self.file_names:
            top_line += 'tf_idf_'+text_title+','
        file.write(top_line+'\n')

        num_cor = len(self.corpus)
        counter = 0
        while num_cor:
            num_cor -= 1
            for word in self.tf_values[counter]:
                under_top = ''
                under_top += word+','
                for word_ in self.tf_values:
                    if word in word_:
                        under_top += str(word_[word])+','
                        continue
                    else:
                        under_top += '0,'

                for word__ in self.idf_values:
                    if word == word__:
                        under_top += str(self.idf_values[word])+','
                        break

                for word___ in self.tf_idf_values:
                    if word in word___:
                        under_top += str(word___[word])+','
                        continue
                    else:
                        under_top += '0,'

                file.write(under_top+'\n')
            counter += 1
        file.close()

    def cosine_distance(self, index_text_1, index_text_2):
        if index_text_1 > (len(self.corpus)-1) or index_text_2 > (len(self.corpus)-1):
            return 1000

        from_both = []
        for potential_word in self.corpus[index_text_1]:
            if potential_word in from_both:
                continue
            else:
                from_both.append(potential_word)
        for potential_second in self.corpus[index_text_2]:
            if potential_second in from_both:
                continue
            else:
                from_both.append(potential_second)

        arrow_one = []
        arrow_two = []
        for word_both in from_both:
            if word_both in self.corpus[index_text_1]:
                arrow_one.append((self.tf_idf_values[index_text_1])[word_both])
            else:
                arrow_one.append(0)
            if word_both in self.corpus[index_text_2]:
                arrow_two.append((self.tf_idf_values[index_text_2])[word_both])
            else:
                arrow_two.append(0)

        arrow_one_two = []
        for numeral in range(0, len(from_both)-1):
            arrow_one_two.append(arrow_one[numeral]*arrow_two[numeral])

        new_arrow_one = []
        new_arrow_two = []
        for numeral in range(0, len(from_both)-1):
            new_arrow_one.append(arrow_one[numeral]**2)
            new_arrow_two.append(arrow_two[numeral]**2)

        upper = 0
        lower_one = 0
        lower_two = 0
        for numeral in range(0, len(from_both)-1):
            upper += arrow_one_two[numeral]
            lower_one += new_arrow_one[numeral]
            lower_two += new_arrow_two[numeral]

        distance = upper / (math.sqrt(lower_one) * math.sqrt(lower_two))
        return distance


#  scenario to check your work
#  test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
#  tf_idf = TfIdfCalculator(test_texts)
#  tf_idf.calculate_tf()
#  tf_idf.calculate_idf()
#  tf_idf.calculate()
#  tf_idf.dump_report_csv()  # - csv checker
#  res = tf_idf.cosine_distance(1, 3)  # - cosine_checker
#  print(res)
#  print(tf_idf.report_on('good', 0))
#  print(tf_idf.report_on('and', 1))
