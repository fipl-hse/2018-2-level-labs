import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
            
def clean_tokenize_corpus(texts):
    list_of_not_words = [
        '!', '@', '#', '$', '%', '^',
        '&', '*', '(', ')', '-', '_',
        '=', '+', '{', '}', '[', ']',
        ',', '.', '/', "'", '"', '<',
        '>', '~', '1', '2', '3', '4',
        '5', '6', '7', '8', '9', '0'
    ]
    if texts is not None:
        clean_list = []
        for sent in texts:
            if isinstance(sent, str) and sent is not None:
                sent = sent.lower()
                sent = sent.replace('<br />', ' ')
                new_sents = ''
                for symbol in sent:
                    if symbol not in list_of_not_words:
                        new_sents += symbol
                new_sents_split = new_sents.split(' ')
                for symb_word in new_sents_split:
                    if symb_word == '':
                        new_sents_split.remove(symb_word)
                clean_list.append(new_sents_split)
        return clean_list
    else:
        return []
    
class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if not isinstance(self.corpus, list) or self.corpus is None:
            return []
        else:
            for piece in self.corpus:
                if piece is not None:
                    tfd = {}
                    c = 0
                    for elm in piece:
                        if isinstance(elm, str):
                            c += 1
                    for word in piece:
                        if isinstance(word, str):
                            tf_n = piece.count(word) / c
                            tfd_1 = {word : tf_n}
                            tfd.update(tfd_1)
                    self.tf_values.append(tfd)
            return self.tf_values

    def calculate_idf(self):
        if self.corpus is None:
            return {}
        else:
            list_of_words = []
            for piece in self.corpus:
                if piece:
                    list_of_words.append(piece)
            full_wrd = []
            for elem in list_of_words:
                for word in elem:
                    if isinstance(word, str):
                        full_wrd.append(word)
            for word in full_wrd:
                f = 0
                if word in self.idf_values:
                    continue
                for current_text in list_of_words:
                    if word in current_text:
                        f += 1
                        continue
                self.idf_values[word] = math.log(len(list_of_words) / f)
            return self.idf_values

    def calculate(self):
        if self.tf_values is None or self.idf_values is None:
            return {}
        elif self.tf_values == [] or self.idf_values == {}:
            return {}
        else:
            for v in self.tf_values:
                tf_idf_value_d = {}
                for word in v:
                    tf_idf_value_d[word] = v[word] * self.idf_values[word]
                self.tf_idf_values.append(tf_idf_value_d)
            return self.tf_idf_values

    def report_on(self, word, document_index):
        if self.tf_idf_values == [] or self.tf_idf_values is None or document_index >= len(self.tf_idf_values):
            return ()
        else:
            list_of_values = []
            for v in self.tf_idf_values[document_index].values():
                list_of_values.append(v)
            sort_v = sorted(list_of_values)
            for k, i in self.tf_idf_values[document_index].items():
                if k == word:
                    first_one = i
                    for i in sort_v:
                        if i == v:
                            second_one = sort_v.index(i)
            result = [first_one, second_one]
            return tuple(result)


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
