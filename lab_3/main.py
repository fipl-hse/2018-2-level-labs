import collections
import more_itertools
import math
cnt = collections.Counter()
if __name__ == '__main__':
  with open('not_so_big_reference_text.txt', 'r') as f:
    REFERENCE_TEXT = f.read()   
TEXT = REFERENCE_TEXT


def split_by_sentence(TEXT):
    restr_chars = "~$%&^@*#\"{}[]\'/\n:.;!?(),<>"
    l_text = TEXT.lower()
    for i in restr_chars:
        if i in l_text:
            if i in '.!?':
                l_text = l_text.replace(i, '.')
            else:
                l_text = l_text.replace(i, '')
    dots = tuple(more_itertools.locate(l_text, lambda x: x == '.'))
    for ind in dots:
        if l_text[int(ind + 1)] == ' ':
            pass
        elif l_text[ind + 1] != None:
            l_text = l_text[:ind] + 'Ê' + l_text[ind + 1:]
        else:
            pass
    l_text = l_text.replace('Ê', '')
    cut_text = l_text.split('.')
    for sentence in range(len(cut_text)):
        cut_text[sentence] = cut_text[sentence].split()
    for element in cut_text:
        if len(element) == 0:
            cut_text.pop(cut_text.index(element))
    for element in cut_text:
        element.append('</s>')
        element.insert(0, '<s>')
    return cut_text


class WordStorage: 
    def __init__(self):
        self.decoding_tab = dict()
        self.counter = 0
        global storage_instance 
        storage_instance = self.decoding_tab
        
        
    def put(self, word):
        if word not in self.decoding_tab.values():
            self.counter = self.counter + 1
            self.decoding_tab.update({self.counter:word})
            return self.counter
        else:
            pass
        
        
    def get_id_of(self, word):
        for k, v in self.decoding_tab.items():
            if word == v:
                return k
        if word not in self.decoding_tab.items():
            return None
            
    def get_original_by(self, number):
        for k, v in self.decoding_tab.items():
            if number == k:
                return v
        if number not in self.decoding_tab.keys():
            return None

    
    def from_corpus(self, cut_text):
        for elements in cut_text:
            for syllabus in elements:
                ws.put(syllabus)
        storage_instance = self.decoding_tab
        return storage_instance


def encode(storage_instance, cut_text):
    corpus = cut_text
    for elements in corpus:
        for syllabus in elements:
            for k,v in storage_instance.items():
                if syllabus == v:
                    elements[elements.index(syllabus)] = k
    return corpus


class NGramTrie:
    def __init__(self):
        self.gram_frequencies = dict()
        self.size = 3
        self.gram_log_probabilities = dict()
        self.chaotic_grams = []
        
        
    def fill_from_sentence(self, corpus):
        for sentence in corpus:
            left = 0
            right = self.size
            while right <= len(sentence):
                self.chaotic_grams.append(tuple(sentence[left:right]))
                left = left + 1
                right = right + 1
                if right > len(sentence):
                    break
        for gram in self.chaotic_grams:
            cnt[gram] += 1
        self.gram_frequencies = dict(cnt)
        return self.gram_frequencies
    
    
    def calculate_log_probabilities(self):
        for k,v in self.gram_frequencies.items():
            self.gram_log_probabilities[k] = round(math.log(v/ len(self.gram_frequencies.values())), 4)

    
    def predict_next_sentence(self, prefix):
        candidates = []
        for gram, log_prob in self.gram_log_probabilities.items():
            if prefix == gram[0:self.size - 1]:
                candidates.append({gram:log_prob})
        
        return candidates


def generate_text(n_gram_model, number_sentences, prefix):
    pass
                

ws = WordStorage()
ngr = NGramTrie()
ws.from_corpus(split_by_sentence(TEXT))
encode(storage_instance, split_by_sentence(TEXT)) 
ngr.fill_from_sentence(encode(storage_instance, split_by_sentence(TEXT)))
ngr.calculate_log_probabilities()
ngr.predict_next_sentence((2,3))