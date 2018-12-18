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
            sentence = sentence.replace('<br />', ' ')
            for element in sentence:
                if element not in list_of_marks:
                    new_text += element
            new_text = new_text.lower()
            splitted_text = new_text.split(' ')
            for word in splitted_text:
                if word == '':
                    splitted_text.remove(word)
            new_list.append(splitted_text)
    return new_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if self.corpus is None:
            return self.tf_values
        for sentence in self.corpus:
            if sentence is not None:
                counter = 0
                freq_dict = {}
                for element in sentence:
                    if type(element) is str:
                        counter += 1
                for word in sentence:
                    if type(word) is str:
                        tf = sentence.count(word) / counter
                        new_dict = {word: tf}
                        freq_dict.update(new_dict)
                self.tf_values.append(freq_dict)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus is None:
            return self.idf_values
        count_sentences = 0
        all_words = []
        for sentence in self.corpus:
            if sentence is not None:
                count_sentences += 1
                for word in sentence:
                    if type(word) is str:
                        all_words.append(word)
        all_words = list(set(all_words))
        for element in all_words:
            count_word = 0
            for text in self.corpus:
                if text is not None:
                    if element in text:
                        count_word += 1
            idf = math.log(count_sentences / count_word)
            little_dict = {element: idf}
            self.idf_values.update(little_dict)
        return self.idf_values

    def calculate(self):
        if self.tf_values == [] or self.idf_values == {}:
            return  self.tf_idf_values
        if self.tf_values is None or self.idf_values is None:
            return self.tf_idf_values
        for the_dict in self.tf_values:
            in_dict = {}
            for key, value in the_dict.items():
                idf_value = self.idf_values[key]
                calc = value * idf_value
                new_dict = {key: calc}
                in_dict.update(new_dict)
            self.tf_idf_values.append(in_dict)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if self.tf_idf_values == [] or self.tf_idf_values is None or document_index >= len(self.tf_idf_values):
            return ()
        values = []
        for value in self.tf_idf_values[document_index].values():
            values.append(value)
        sorted_val = sorted(values)
        for key, index in self.tf_idf_values[document_index].items():
            if key == word:
                first = index
                for i in sorted_val:
                    if i == value:
                        second = sorted_val.index(i)
        final = [first, second]
        return tuple(final)
    
    def dump_report_csv(self):
        excel_file = open('report.csv', 'w')
        first_line = 'word,'
        for text in self.file_names:
            first_line += 'tf' + text + ','
        first_line += 'idf,'
        for text in self.file_names:
            first_line += 'tf_idf' + text + ','
        last_coma = first_line[-1]
        first_line = first_line.replace(last_coma, '\n')
        excel_file.write(first_line)
        for text in self.file_names:
            for word in text:
                second_line = word + ','
                
        excel_file.close

# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
