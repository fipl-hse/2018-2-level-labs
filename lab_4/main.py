import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    texts_list = []
    try:
        for text in texts:
            try:
                if '<br />' in text:
                    text = text.replace('<br />', ' ')
                text = text.lower()
                for symbol in text:
                    if symbol not in 'abcdefghijklmnopqrstuvwxyz ':
                        text = text.replace(symbol, '')
                tokens_list = text.split()
                texts_list.append(tokens_list)
            except TypeError:
                continue
            except AttributeError:
                continue
    except TypeError:
        pass
    return texts_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if self.corpus is None:
            return []
        for text in self.corpus:
            if text is None:
                continue
            only_words_from_text = []
            tf_one_text = {}
            for word in text:
                if isinstance(word, str):
                    only_words_from_text.append(word)
            for new_word in only_words_from_text:
                term_frequency = only_words_from_text.count(new_word) / len(only_words_from_text)
                tf_one_text[new_word] = term_frequency
            self.tf_values.append(tf_one_text)
        return self.tf_values

    def calculate_idf(self):
        corpus_word_list = []
        clear_corpus = []
        if self.corpus is None:
            return {}
        for text in self.corpus:
            if text is not None:
                clear_corpus.append(text)
                for word in text:
                    if isinstance(word, str) and word not in corpus_word_list:
                        corpus_word_list.append(word)
        for word_to_count in corpus_word_list:
            text_counter = 0
            for text in clear_corpus:
                if word_to_count is not None and word_to_count in text:
                    text_counter += 1
            inversed_document_frequency = math.log(len(clear_corpus) / text_counter)
            self.idf_values[word_to_count] = inversed_document_frequency
        return self.idf_values

    def calculate(self):
        if self.tf_values is None:
            return []
        for text_tf in self.tf_values:
            tf_one_text = {}
            for word in text_tf.keys():
                if word in self.idf_values:
                    word_idf = self.idf_values[word]
                    word_tf_idf = text_tf[word] * self.idf_values[word]
                    tf_one_text[word] = word_tf_idf
            if tf_one_text != {}:
                self.tf_idf_values.append(tf_one_text)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        word_tf_idf = 0
        if document_index >= len(self.corpus) or self.tf_idf_values == [] or self.tf_idf_values is None:
            return ()
        if word in self.corpus[document_index]:
            for key, tf_idf in self.tf_idf_values[document_index].items():
                if key == word:
                    word_tf_idf = tf_idf
        tf_idf_rating = []
        words_rating = []
        for tf_idf in self.tf_idf_values[document_index].values():
            tf_idf_rating.append(tf_idf)
        for key in self.tf_idf_values[document_index].keys():
            if self.tf_idf_values[document_index][key] == max(tf_idf_rating):
                words_rating.append(key)
                tf_idf_rating.remove(max(tf_idf_rating))
        word_position = words_rating.index(word)
        if word_tf_idf != 0:
            return tuple([word_tf_idf, word_position])
        else:
            return tuple([None, word_position])


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
