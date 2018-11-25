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
    def put(self, word: str) -> int:
        pass

    def get_id_of(self, word: str) -> int:
        pass

    def get_original_by(self, id: int) -> str:
        pass

    def from_corpus(self, corpus: tuple):
        pass


class NGramTrie:
    def fill_from_sentence(self, sentence: tuple) -> str:
        pass

    def calculate_log_probabilities(self):
        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        pass


def encode(storage_instance, corpus) -> list:
    pass


def split_by_sentence(text):
    if text == None or text == '':
        return []
    else:
        text_0 = text[:]
        text_1 = text_0.replace('\n', '')
        splitted_sentences = []
        separate_sentence = '<s> '
        text_2 = text_1.lower()
        old_tokens = text_2.split(' ')
        for token in old_tokens:
            if token == '':
                old_tokens.remove(token)
        for index, token in enumerate(old_tokens):
            if token.isalnum():
                separate_sentence += token + ' '
            elif ',' in token:
                separate_sentence += token + ' '
            elif '’' in token:
                separate_sentence += token + ' '
            elif "'" in token:
                separate_sentence += token + ' '
            elif '#' in token:
                separate_sentence += token + ' '
            elif '$' in token:
                separate_sentence += token + ' '
            else:
                separate_sentence += token + ' </s>'
                splitted_sentences.append(separate_sentence)
                separate_sentence = '<s> '

        list_sent = []
        for sentence in splitted_sentences:
            list_sent.append(list(sentence))
        for sent in list_sent:
            for element in sent[4:-4]:
                if (element.isalnum() or element == ' ') is False:
                    sent.remove(element)

        clean_sentences = []
        for element1 in list_sent:
            clean_sentences.append(''.join(element1))

        tokenized_sents = []
        for element2 in clean_sentences:
            tokenized_sent = element2.split(' ')
            if tokenized_sent != ['<s>', '', '</s>']:
                tokenized_sents.append(tokenized_sent)
        return tokenized_sents
    pass
