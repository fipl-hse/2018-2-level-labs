import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts):
  reviews = []  # a list of texts to clean

  paragraphs = []  # getting rid of the break signs between paragraphs
  try:
      for t in texts:
          if type(t) is not str:
              texts.remove(t)
  except:
      return []
  try:
      for t in texts:
          try:
              paragraph = t.split('<br /><br />')
              paragraphs.append(paragraph)
          except:
              paragraphs = []

      raw_reviews = []  #joining them back
      for p in paragraphs:
          try:
              raw_review = ' '.join(p)
              raw_reviews.append(raw_review)
          except:
              raw_reviews = []

      for r_r in raw_reviews:
          try:
              review = r_r.split(' ')
              reviews.append(review)  #getting a list of lists
          except:
              reviews = []

      clean_reviews = []
      for r in reviews:
          clean_review = []
          for w in r:
              try:
                  w = w.lower()
                  word = ''  #clean word iterable
              except:
                  word = ''
              try:
                  for symbol in w:
                      if symbol.isalpha():
                          word += symbol
                  if word != '':
                      clean_review.append(word)
              except:
                  clean_review = []
          clean_reviews.append(clean_review)
  except:
      clean_reviews = []
  return clean_reviews



class TfIdfCalculator:
    def __init__(self, corpus):
        pass

    def calculate_tf(self):
        pass

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
