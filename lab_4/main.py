import math
import re
import collections
import pandas as pd
REFERENCE_TEXTS = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())


def clean_tokenize_corpus(texts: list) -> list:
    restr_chars = "~$%&^@*#\"{}[]\'/\n:=-.;!?(),<>"
    cleanr = re.compile('<.*?>')
    if texts is None:
        return []
    for elem in texts:
        if elem is None:
            del texts[texts.index(elem)]
    if not all(isinstance(elem, str) for elem in texts):
        del texts[texts.index(elem)]
    if not all(isinstance(x, str) or None for x in texts):
        return []
    if all(x is None for x in texts):
        return []
    l_text = [list(filter(lambda i: i not in restr_chars, re.sub(cleanr, ' ', chunk.lower()))) for chunk in texts]
    l_text = [(''.join(chunks)).split() for chunks in l_text]
    return l_text
    


class TfIdfCalculator:
    def __init__(self, n):
        self.corpus = n
        self.tf_values = []
        self.tf_undertaken = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.verse_counter = {}

    def calculate_tf(self):
        if self.corpus is None or all(chunk is None for chunk in self.corpus):
            return []
        for elem in self.corpus:
            if elem is None:
                del self.corpus[self.corpus.index(elem)]
                continue
            for word in elem:
                if not isinstance(word, str) or None:
                    del elem[elem.index(word)]
        for chunk in self.corpus:
            cnt = collections.Counter()
            for word in chunk:
                cnt[word] += 1
            self.tf_undertaken.append(dict(cnt))
        for parced_text in self.tf_undertaken:
            clear_tmp = {}
            for word, tf in parced_text.items():
                if isinstance(word, str):
                    clear_tmp[word] = tf
            tempo_value = {}
            for word, freq in clear_tmp.items():
                tempo_value[word] = float(freq) / (sum(clear_tmp.values()))
            self.tf_values.append(tempo_value)

    def calculate_idf(self):
        if self.corpus is None or all(chunk is None for chunk in self.corpus):
            return []
        for elem in self.corpus:
            if elem is None:
                del self.corpus[self.corpus.index(elem)]
                continue
            for word in elem:
                if not isinstance(word, str) or None:
                    del elem[elem.index(word)]
        verse = set()
        for chunk in self.corpus:
            for word in chunk:
                verse.add(word)
        for token in verse:
            self.verse_counter[token] = 0
        for sylla in verse:
            for chunk in self.corpus:
                if sylla in chunk:
                    self.verse_counter[sylla] += 1
        for word, counter in self.verse_counter.items():
            self.idf_values[word] = math.log(float(len(self.corpus)) / counter)

    def calculate(self):
        if self.idf_values and self.tf_values:
            for chunk in self.tf_values:   
                temp_fold = {}
                for key in self.idf_values.keys():
                    if key in chunk:
                        temp_fold[key] = chunk.get(key) * self.idf_values.get(key)
                self.tf_idf_values.append(temp_fold)
                
    def report_on(self, word, document_index):
        try: 
            self.tf_idf_values[document_index]
        except:
            return () 
        if not self.tf_idf_values:
            return ()
        part = self.tf_idf_values[document_index]
        word_orderal = int(part.get(word))
        order = sorted(part.values(), reverse=True)
        return (word_orderal, order.index(word_orderal))
    
    def dump_report_csv(self):
        d_c = {'word': pd.Series(list(self.idf_values.keys())), 
             'IDF': pd.Series(list(self.idf_values.values()))}
        
        for chunk in range(len(self.tf_values)):
            tf = self.tf_values[chunk]
            d_c['TF'+ '(' + str(texts[chunk]) + ')'] = pd.Series(list(tf.values()))
            
        for chunkee in range(len(self.tf_idf_values)):
            tfidf = self.tf_idf_values[chunkee]
            d_c['TF-IDF'+ '(' + str(texts[chunkee]) + ')'] = pd.Series(list(tfidf.values()))
            
        tfs = ['TF'+ '(' + str(chunks) + ')' for chunks in texts]
        tfidfs = ['TF-IDF'+ '(' + str(chunks) + ')' for chunks in texts]
        columns = ['word'] + tfs + ['IDF'] + tfidfs 
        data = pd.DataFrame(d_c, columns=columns)
        data.to_csv('report.csv', sep='\t', encoding='utf-8')            
        
        
        
        
                
        


# scenario to check your work
test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
tf_idf = TfIdfCalculator(test_texts)
tf_idf.calculate_tf()
tf_idf.calculate_idf()
tf_idf.calculate()
print(tf_idf.report_on('good', 0))
print(tf_idf.report_on('and', 1))
print (test_texts)
tf_idf.dump_report_csv()


