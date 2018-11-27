"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.number_of_id = 0
        self.storage = {}
    def put(self, word):
        if isinstance(word, str) is False or word in self.storage:
            return self.storage
        for value in self.storage.values():
            if value == self.number_of_id:
                self.number_of_id += 1
        self.storage[word] = self.number_of_id
        return self.number_of_id
    def get_id_of(self, word):
        if word not in self.storage.keys():
            return -1
        return self.storage[word]
    def get_original_by(self, id):
        for number_of_id, word in self.storage.items():
            if number_of_id == id:
                return word
        if id not in self.storage.values():
            return 'UNK'
    def from_corpus(self, corpus):
        if corpus is None or isinstance(corpus, tuple) is False:
            return {}
        for word in corpus:
            self.put(word)
          
class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_log_probabilities = {}
        self.gram_frequencies = {}
    def fill_from_sentence(self, sentence):
        if sentence is not None and isinstance(sentence, tuple) is True and sentence != ():
            ngram_listed = []
            d = self.size
            cntr = 0
            while cntr != len(sentence) - d + 1:
                ngram_listed.append(sentence[cntr:cntr] + d)
                cntr += 1
            for member in ngram_listed:
                frequent = ngram_listed.count(member)
                self.gram_frequencies[member] = frequent
            return 'OK'
        else:
            return 'ERROR'
    def calculate_log_probabilities(self):
        if self.gram_frequencies != {}:
            list_of_ngrams = []
            count_num = 1
            for key, value in self.gram_frequencies.items():
                val = value
                if val == 1:
                    list_of_ngrams.append(key)
                elif val > 1:
                    while count_num != val + 1:
                        list_of_ngrams.append(key)
                        count_num += 1
            for b in list_of_ngrams:
                start = 0
                for b_2 in list_of_ngrams:
                    if b[:-1] == b_2[:-1]:
                        start += 1
                b_number = self.gram_frequencies[b]
                prob = math.log(b_number / start)
                self.gram_log_probabilities[b] = prob
            return self.gram_log_probabilities
        else:
            return {}
    def predict_next_sentence(self, prefix):
        if self.gram_log_probabilities is None or self.gram_log_probabilities == {}:
            return []
        prefix = list(prefix)
        counter = 0
        list_of_values = []
        list_of_two = []
        for key in self.gram_log_probabilities.keys():
            list_of_two.append(key)
        while counter != len(list_of_two ):
            for n_gram in list_of_two :
                if n_gram[0] == prefix[-1]:
                    list_of_values.append(self.gram_log_probabilities[n_gram])
            if list_of_values == []:
                return prefix
            max_val = max(list_of_values)
            for key, value in self.gram_log_probabilities.items():
                if value == max_val:
                    prefix.append(key[-1])
            list_of_values = []
            counter += 1
        return prefix
       
def encode(storage_instance, corpus):
    if storage_instance is not None and corpus is not None:
        coded_list = []
        for sents in corpus:
            for key, value in storage_instance.items():
                if key in sents:
                    coded_list.append(storage_instance[key])
            return coded_list
    else:
        return []
     
def split_by_sentence(text):
    if text is not None and text != '':
        text_1 = text[:]
        text_2 = text_1.replace('\n', '')
        text_3 = text_2.lower()
        all_sentences = []
        divided_sentence = '<s> '
        all_tokens = text_3.split(' ')
        for word in all_tokens:
            if word == '':
                all_tokens.remove(word)
        for pointer, word in enumerate(all_tokens):
            if word.isalnum():
                divided_sentence += word + ' '
            elif ',' in word:
                divided_sentence += word + ' '
            elif '$' in word:
                divided_sentence += word + ' '
            elif '#' in word:
                divided_sentence += word + ' '
            elif '-' in word:
                divided_sentence += word + ' '
            elif "'" in word:
                divided_sentence += word + ' '
            elif ':' in word:
                divided_sentence += word + ' '
            elif '’' in word:
                divided_sentence += word + ' '
            elif '*' in word:
                divided_sentence += word + ' '
            elif '_' in word:
                divided_sentence += word + ' '
            else:
                divided_sentence += word + '</s>'
                all_sentences.append(divided_sentence)
                divided_sentence = '<s> '
    else:
        return []
    list_of_sents = []
    for sentence in all_sentences:
        list_of_sents.append(list(sentence))
    for sentence in list_of_sents:
        for symbol in sentence[4:-4]:
            if symbol.isalnum() is False and symbol != ' ':
                sentence.remove(symbol)
    clear_sentences = []
    for symbol_1 in list_of_sents:
        clear_sentences.append(''.join(symbol_1))
    tok_sents = []
    for symbol_2 in clear_sentences:
        tok_sent = symbol_2.split(' ')
        if tok_sent != ['<s>', '', '</s>']:
            tok_sents.append(tok_sent)
    return tok_sents
