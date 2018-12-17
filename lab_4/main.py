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
        pass

    def calculate(self):
        pass

    def report_on(self, word, document_index):
        pass


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
