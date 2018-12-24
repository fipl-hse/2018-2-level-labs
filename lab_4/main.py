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

    all_new = []
    if texts is None:
        return all_new
    for sentence in texts:
        if sentence == str(sentence) and sentence is not None:
            all_new = ''
            sentence = sentence.lower()
            sentence = sentence.replace('<br />', ' ')
            for e in sentence:
                if e not in list_of_marks:
                    all_new += e
            new_text = all_new.lower()
            txt_separate = new_text.split(' ')
            for word in txt_separate:
                if word == '':
                    txt_separate.remove(word)
            all_new.append(txt_separate)
    return all_new


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        for text in self.corpus:
            tf_text = {}
            len_text = len(text)

            for word in text:
                if word in tf_text:
                    tf_text[word] += 1 / len_text
                else:
                    tf_text[word] = 1 / len_text
            self.tf_values.append(tf_text)
        return

    def calculate_idf(self):
        if self.corpus is None:
            return {}
        new_corpus = []
        for first_txt in self.corpus:
            if first_txt:
                new_corpus.append(first_txt)
        _words = []
        for second_txt in new_corpus:
            for word in second_txt:
                if isinstance(word, str):
                    _words.append(word)
        for word in _words:
            word_freq = 0
            if word in self.idf_values:
                continue
            for third_text in new_corpus:
                if word in third_text:
                    word_freq += 1
                    continue
            self.idf_values[word] = math.log(len(new_corpus) / word_freq)

    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return

        for tf_dict in self.tf_values:
            tf_idf_dict = {}
            for key, value in tf_dict.items():
                tf_idf_dict[key] = value * self.idf_values[key]
            self.tf_idf_values.append(tf_idf_dict)

        return

    def report_on(self, word, document_index):
        if self.tf_idf_values == [] or self.tf_idf_values is None:
            return ()
        if document_index > len(self.corpus) - 1:
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


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
