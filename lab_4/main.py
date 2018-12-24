import math

REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())

def clean_tokenize_corpus(texts: list) -> list:
    pass
    token_corpus = []
    try:
        for o_text in texts:
            try:
                if '<br/>' in o_text:
                    o_text = o_text.replace('<br/>', ' ')
                o_text = o_text.lower()
                for element in o_text:
                    if element not in 'qwertyuiopasdfghjklzxcvbnm':
                        o_text = o_text.replace(element, '')
                token_texts = o_text.split()
                token_corpus.append(token_texts)
            except TypeError:
                continue
            except AttributeError:
                continue
    except TypeError:
        pass
    return token_corpus
    #token_corpus = []
   # if texts and isinstance(texts, list):
       # for o_text in texts:
   #         if o_text and isinstance(o_text, str):
       #         while '<br/>' in o_text:
   #                 o_text = o_text.replace('<br/>', ' ')
    #            token_texts = []
     #           itog_text = o_text.split(' ')
      #          for element in itog_text:
       #             element = element.lower()
        #            new_element = ''
         #           if element == 'br' or element == 'n':
          #              continue
           #         else:
            #            token_texts.append(element)
             #       if not element.isalpha():
              #          for i in element:
               #             if i.isalpha():
                #                new_element += i
                 #       if new_element:
                  #          token_texts.append(new_element.lower())
                   # else:
                    #    token_texts.append(element.lower())
             #   token_corpus += [token_texts]
       # return token_corpus
  #  else:
   #     return token_corpus

class TfIdfCalculator:
    def __init__(self, corpus):
        pass
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        pass
        if not isinstance(self.corpus, list):
            return []
        if isinstance(self.corpus, list):
            for o_text in self.corpus:
                if not isinstance(o_text, list):
                    continue
                tf_dict = {}
                elements_list = []
                for element in o_text:
                    if isinstance(element, str):
                        elements_list.append(element)
                for new_element in elements_list:
                    tf_value = elements_list.count(new_element)
                    tf_dict[new_element] = tf_value / len(elements_list)
                self.tf_values.append(tf_dict)

    def calculate_idf(self):
        pass
        idf_list = []
        if self.corpus is None:
            return {}
        if isinstance(self.corpus, list):
            for o_text in self.corpus:
                if o_text:
                    idf_list.append(o_text)
            element_idf_list = []
            for word in idf_list:
                for element in word:
                    if isinstance(element, str):
                        element_idf_list.append(element)
            for count in element_idf_list:
                o_text_counter = 0
                if count in self.idf_values:
                    continue
                for new_text in idf_list:
                    if count in new_text:
                        o_text_counter += 1
                        continue
                idf_value = math.log(len(idf_list) / o_text_counter)
                self.idf_values[count] = idf_value

    def calculate(self):
        pass
        if self.tf_values == [] or self.tf_values is None:
            return []
        if self.idf_values == {} or self.idf_values is None:
            return []
        for tf_dict in self.tf_values:
            tf_idf_dict = {}
            for element in tf_dict:
                tf_idf_dict[element] = tf_dict[element] * self.idf_values[element]
            self.tf_idf_values.append(tf_idf_dict)

    def report_on(self, word, document_index):
        pass
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        result_list = []
        tf_idf_doc = self.tf_idf_values[document_index]
        for key, value in tf_idf_doc.items():
            result_list.append((value, key))
        result_list.sort(reverse=True)
        counter = -1
        for number in result_list:
            counter += 1
            if number[1] == word:
                return number[0], counter

# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
