"""
Labour work #3
 Building an own N-gram model
"""
import random
import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.word = ''
        self.id_num = 0
        self.storage = {}

    def put(self, word: str) -> int:
        if word is None:
            return None
        elif type(word) != str:
            return {}
        else:
            if word in self.storage.keys():
                return self.storage[word]
            else:
                new_id = random.randint(1, 1000000)
                while new_id in self.storage.values():
                    new_id = random.randint(1, 1000000)
                self.storage[word] = new_id
                return self.storage[word]
        pass

    def get_id_of(self, word: str) -> int:
        if word is None or type(word) != str:
            return -1
        else:
            if word in self.storage.keys():
                return self.storage[word]
            else:
                return -1
        pass

    def get_original_by(self, id: int) -> str:
        list_of_words_id = []
        for k, v in self.storage.items():
            list_of_words_id.append([k, v])
        for pair in list_of_words_id:
            if id == pair[1]:
                return pair[0]
        else:
            return 'UNK'
        pass

    def from_corpus(self, corpus: tuple):
        if corpus is None or type(corpus) != tuple:
            return {}
        else:
            just_words = []
            for word in corpus:
                just_words.append(word)
            no_duplicates = set(just_words)
            clear_ordered = list(no_duplicates)
            words = []
            ids = []
            for element in clear_ordered:
                self.word = element
                self.id_num += 1
                words.append(self.word)
                ids.append(self.id_num)
            self.storage = dict(zip(words, ids))
            return self.storage
        pass



class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

 
    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence is None or sentence == () or type(sentence) != tuple:
            return 'ERROR'
        else:
            n = self.size
            k = 0
            ngram = []
            while k != len(sentence) - n + 1:
                ngram.append(sentence[k:k + n])
                k += 1
            for elmnt in ngram:
                freq = ngram.count(elmnt)
                self.gram_frequencies[elmnt] = freq
            return 'OK'
        pass

    def calculate_log_probabilities(self):
        ngrams = []
        counter = 0
        if self.gram_frequencies == {} or self.gram_frequencies is None:
            return {}
        else:
            for key, value in self.gram_frequencies.items():
                v = value
                if v == 1:
                    ngrams.append(key)
                elif v > 1:
                    while counter < v:
                        ngrams.append(key)
                        counter += 1
                    counter = 0
            same_beginning = 0
            for t in ngrams:
                if t[:-1] == ngrams[0][:-1]:
                    same_beginning += 1
                else:
                    continue
            for t in ngrams:
                t_quantity = self.gram_frequencies[t]
                probability = math.log(t_quantity / same_beginning)
                self.gram_log_probabilities[t] = probability
            return self.gram_log_probabilities

        pass

    def predict_next_sentence(self, prefix: tuple) -> list:
        probabilities_k = []
        similar_beginning = {}
        if prefix is None or type(prefix) != tuple:
            return []
        else:
            predicted = list(prefix)
            helper = []
            helper.append(predicted[-1])
            if len(prefix) != self.size - 1:
                return []
            else:
                for key_p in self.gram_log_probabilities.keys():
                    probabilities_k.append(key_p[:self.size - 1])
                    probabilities_k2 = set(probabilities_k)
                while tuple(helper) in probabilities_k2:
                    for key, value in self.gram_log_probabilities.items():
                        helper2 = []
                        helper2.append(predicted[-1])
                        if list(key[:self.size - 1]) == helper2:
                            similar_beginning[key] = value
                        ks = []
                        vs = []
                    for k, v in similar_beginning.items():
                        ks.append(k)
                        vs.append(v)
                        winner = max(vs)
                        w_ind = vs.index(winner)
                        if ks[w_ind][-1] not in predicted:
                            predicted.append(ks[w_ind][-1])
                        similar_beginning = {}
                    probabilities_k2.remove(tuple(helper))
                    helper = []
                    helper.append(predicted[-1])
                return predicted
        pass


def encode(storage_instance, corpus) -> list:
    if (storage_instance is None or corpus is None):
        return []
    else:
        encoded = []
        for sent in corpus:
            for key, value in storage_instance.items():
                if key in sent:
                    encoded.append(storage_instance[key])
        return encoded
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
