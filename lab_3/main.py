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
    def put(self, word):

    def get_id_of(self, word):

    def get_original_by(self, id):

    def from_corpus(self, corpus):


class NGramTrie:
    def fill_from_sentence(self, sentence):

    def calculate_log_probabilities(self):

    def predict_next_sentence(self, prefix):


def encode(storage_instance, corpus):
     if storage_instance is not None and corpus is not None:
        coded_list = []
        for sentence in corpus:
            for key, value in storage_instance.items():
                if key in sentence:
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
            elif "'" in word:
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
