import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts):
      try:
        reviews = []
        paragraphs = []
        for t in texts:
            try:
                paragraph = t.split('<br /><br />')
                paragraphs.append(paragraph)
            except:
                paragraphs.append([])


        raw_reviews = []
        for p in paragraphs:
            raw_review = ' '.join(p)
            raw_reviews.append(raw_review)
       
        for r_r in raw_reviews:
            review = r_r.split(' ')
            reviews.append(review)

        clean_reviews = []
        for review in reviews:
            clean_review = []
            for w in review:
                w = w.lower()
                word = ''
                for symbol in w:
                    if symbol.isalpha():
                        word += symbol
                if word != '':
                    clean_review.append(word)
            if clean_review != []:
                clean_reviews.append(clean_review)
    except:
        clean_reviews = []
    return clean_reviews



class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        try:
            words_quantity = []
            no_duplicates_corpus = []
            for text in self.corpus:
                num_of_words = 0
                no_duplicates_text = []
                try:
                    for word in text:
                        if type(word) is str:
                            num_of_words += 1
                        if word not in no_duplicates_text and word != '' and type(word) is str:
                            no_duplicates_text.append(word)
                except:
                    no_duplicates_text = []
                no_duplicates_corpus.append(no_duplicates_text)
                words_quantity.append(num_of_words)

            frequencies = []
            for ind, text in enumerate(no_duplicates_corpus):
                frequencies_review = []
                for token in text:
                    i = 0
                    while i < len(self.corpus):
                        frequency = self.corpus[ind].count(token)
                        i += 1
                    tf = frequency/words_quantity[ind]
                    frequencies_review.append(tf)
                frequencies.append(frequencies_review)
            tf_for_each_text = []
            for index, text in enumerate(no_duplicates_corpus):
                dictionary = dict(zip(no_duplicates_corpus[index], frequencies[index]))
                if dictionary != {}:
                    tf_for_each_text.append(dictionary)
        except:
            tf_for_each_text = []
        self.tf_values = tf_for_each_text


    def calculate_idf(self):
                try:
            num_of_docs = 0
            for text in self.corpus:
                if type(text) is list and text != []:
                    num_of_docs += 1

            no_duplicates_corpus = []
            for text in self.corpus:
                no_duplicates_text = []
                try:
                    for word in text:
                        if word not in no_duplicates_text and word != '' and type(word) is str:
                            no_duplicates_text.append(word)
                except:
                    no_duplicates_text = []
                no_duplicates_corpus.append(no_duplicates_text)

            frequencies_corpus = []
            for text in no_duplicates_corpus:
                frequencies_review = []
                for token in text:
                    frequency = 0
                    for review in self.corpus:
                        try:
                            if token in review:
                                frequency += 1
                        except:
                            frequency = 0
                    frequencies_review.append(frequency)
                frequencies_corpus.append(frequencies_review)

            idf = []
            for text in frequencies_corpus:
                idf_text = []
                for freq in text:
                    idf_text.append(math.log(num_of_docs / freq))
                idf.append(idf_text)

            idf_for_each_text = []
            for index, text in enumerate(no_duplicates_corpus):
                dictionary = dict(zip(no_duplicates_corpus[index], idf[index]))
                if dictionary != {}:
                    idf_for_each_text.append(dictionary)
            idf_dict = {}
            for i in idf_for_each_text:
                for key, value in i.items():
                    idf_dict[key] = value
        except:
            idf_dict = {}
        self.idf_values = idf_dict

    def calculate(self):
        try:
            no_duplicates_corpus = []
            for text in self.corpus:
                no_duplicates_text = []
                try:
                    for word in text:
                        if word not in no_duplicates_text and word != '' and type(word) is str:
                            no_duplicates_text.append(word)
                except:
                    no_duplicates_text = []
                no_duplicates_corpus.append(no_duplicates_text)

            tf_idf_list = []
            #print(self.tf_values)
            for text in self.tf_values:
                tf_idf_review = {}
                for token, v in text.items():
                    try:
                        tf_idf_review[token] = v * self.idf_values[token]
                    except:
                        pass
                if tf_idf_review != {}:
                    tf_idf_list.append(tf_idf_review)
        except:
            tf_idf_list = []
        self.tf_idf_values = tf_idf_list

    def report_on(self, word, document_index):
        no_duplicates_corpus = []
        if document_index < len(self.corpus):
            if word not in self.corpus[document_index]:
                return ()
        for text in self.corpus:
            no_duplicates_text = []
            try:
                for token in text:
                    if token not in no_duplicates_text and token != '' and type(token) is str:
                        no_duplicates_text.append(token)
            except:
                no_duplicates_text = []
            no_duplicates_corpus.append(no_duplicates_text)

        freqs = []
        freqs_list_all = []
        for ind, text in enumerate(no_duplicates_corpus):
            freqs_text = {}
            freqs_list = []
            for token in text:
                i = 0
                while i < len(self.corpus):
                    freq = self.corpus[ind].count(token)
                    i += 1
                freqs_text[token] = freq
                if freq not in freqs_list:
                    freqs_list.append(freq)
            freqs.append(freqs_text)
            freqs_list_all.append(freqs_list)

        big_helper = []
        for text in freqs_list_all:
            helper_d = {}
            text.sort()
            c = len(text)
            while c != 0:
                for i in text:
                    helper_d[i] = c - 1
                    c -= 1
            big_helper.append(helper_d)

        ratings = []
        for ind, text in enumerate(freqs):
            rating = {}
            for el, v in text.items():
                rating[el] = big_helper[ind][v]
            ratings.append(rating)

        try:
            tf_idf = self.tf_idf_values[document_index][word]
        except:
            tf_idf = None
        # print(ratings[document_index])
        try:
            rate = ratings[document_index][word]
        except:
            rate = None
        # print(rate)
        if tf_idf != None and rate != None:
            report = (tf_idf, rate)
        else:
            report = ()


        return report


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
