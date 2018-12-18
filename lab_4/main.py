import re
import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    if not texts:
        return []

    for text in texts:
        if text is None or not isinstance(text, str):
            texts.remove(text)

    clean_texts = []

    for text in texts:
        if isinstance(text, str):
            text = re.sub(r'\n', '', text)
            text = re.sub(r'<br />', ' ', text)
            text = re.sub(r'[,!:;`~@#$%^&*+=''><()-]', '', text)
            clean_texts.append(text)

    clean_tokenized_texts = []
    for text in clean_texts:
        token = re.split(r'\W+', text)
        clean_tokenized_texts.append(token)

    final_corpus = []
    for text in clean_tokenized_texts:
        new_text = [token.lower() for token in text]
        final_corpus.append(new_text)

    # delete last empty list
    for text in final_corpus:
        while '' in text:
            text.remove('')

    return final_corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus and isinstance(self.corpus, list):
            for part in self.corpus:
                if part is not None:
                    len_of_text = 0
                    freq_dict = {}
                    for word in part:
                        if isinstance(word, str):
                            len_of_text += 1
                            if word not in freq_dict:
                                freq_dict[word] = 1
                            else:
                                new_word = freq_dict[word] + 1
                                freq_dict[word] = new_word

                    for word, freq in freq_dict.items():
                        freq_dict[word] = freq / len_of_text

                    self.tf_values.append(freq_dict)

    def calculate_idf(self):
        if self.corpus and isinstance(self.corpus, list):
            len_of_corpus = 0
            for part in self.corpus:
                if isinstance(part, list):
                    len_of_corpus += 1
            for part in self.corpus:
                if part is not None:
                    for word in part:
                        if isinstance(word, str):
                            if word not in self.idf_values.keys():
                                occurrence_counter = 0
                                for text_to_compare in self.corpus:
                                    if text_to_compare:
                                        if word in text_to_compare:
                                            occurrence_counter += 1
                                self.idf_values[word] = math.log(len_of_corpus / occurrence_counter)

    def calculate(self):
        if self.tf_values and self.idf_values:
            for tf_dict in self.tf_values:
                particular_dict = {}
                for word, tf_value in tf_dict.items():
                    if self.idf_values[word]:
                        particular_dict[word] = tf_value * self.idf_values[word]
                    else:
                        particular_dict[word] = 0
                self.tf_idf_values.append(particular_dict)

    def report_on(self, word, document_index):
        final_tuple = tuple()
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        else:
            current_tf_idf = self.tf_idf_values[document_index].get(word)
            place = 0
            if current_tf_idf is not None:
                for one_tf_idf in self.tf_idf_values[document_index].values():
                    if current_tf_idf < one_tf_idf:
                        place += 1
            return current_tf_idf, place


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
