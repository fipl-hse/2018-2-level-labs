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
        self.storage = {}
        self.id = 0


    def put(self, word: str) -> int:

        # return error value if incorrect argument was provided
        if (type(word) is not str) or (word in ['', None]):
            return -1

        # if the word is already stored, return its id
        if word in self.storage:
            return self.storage[word]

        # otherwise add the new element to the storage
        self.id += 1
        self.storage[word] = self.id
        return self.id



    def get_id_of(self, word: str) -> int:

        # return error value if incorrect argument was provided or the word is not in storage
        if (type(word) is not str) or (word in ['', None]) or (word not in self.storage):
            return -1

        return self.storage[word]



    def get_original_by(self, id: int) -> str:

        # return error value if incorrect argument was provided
        if type(id) is not int:
            return 'UNK'

        # look up for the item with requested id in the storage
        for key, value in self.storage.items():
            if value == id:
                return key
        return 'UNK'



    def from_corpus(self, corpus: tuple):

        # return error value if incorrect argument was provided
        if type(corpus) is not tuple:
            return {}

        # add all corpus elements in the list
        for word in corpus:
            self.put(word)


class NGramTrie:

    def __init__(self, N):
        self.size = N
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}


    def fill_from_sentence(self, sentence: tuple) -> str:

        if type (sentence) is not tuple:
            return 'ERROR'

        for index in range (0, len(sentence)-self.size+1):

            ngram = sentence[index:index+self.size]

            if ngram in self.gram_frequencies:
                # increase # of appearances if already in the dictionary
                self.gram_frequencies[ngram] += 1
            else:
                # register first appearance if not yet in the dictionary
                self.gram_frequencies[ngram] = 1

        return 'OK'



    def calculate_log_probabilities(self):

        for key1 in self.gram_frequencies.keys():

            denominator = 0
            for key2 in self.gram_frequencies.keys():

                # if N-1 elements of the keys are equal, increasing the denominator by second key frequencies
                if key1[:-1] == key2[:-1]:
                    denominator += self.gram_frequencies[key2]

            # populate the probability
            self.gram_log_probabilities[key1] = math.log(self.gram_frequencies[key1] / denominator)


    def predict_next_sentence(self, prefix: tuple) -> list:

        # check if prefix type and size is correct and probabilities are populated
        if (type(prefix) is not tuple) or (len(prefix) != self.size-1) or (self.gram_log_probabilities == {}):
            return []

        predicted_sentence = list(prefix)
        predicted_sentence_len = 0

        while predicted_sentence_len != len(predicted_sentence):  # continue while we still can add new items (length is changing)

            predicted_sentence_len = len(predicted_sentence)

            # go through the pairs sorted by descending probabilities
            for key, value in sorted(self.gram_log_probabilities.items(), key=lambda item: -item[1]):
                key_list=list(key)

                # choose the first key (top probability) starting with last (size-1) items of the predicted sentence
                if key_list[:-1] == predicted_sentence[-(self.size-1):]:

                    # add the last item from the key to the sentence and continue to build sentence further
                    predicted_sentence.append(key[-1])
                    break

        return predicted_sentence


def encode(storage_instance, corpus) -> list:

    encoded_corpus = []

    for sentence in corpus:
        encoded_sentence = []
        for word in sentence:
            word_id = storage_instance.put(word)
            encoded_sentence.append(word_id)
        encoded_corpus.append(encoded_sentence)

    return encoded_corpus


def split_by_sentence(text: str) -> list:

    # checking if input string is not empty and is terminated as a sentence by . or ? or !
    if text in ['', None]:
        return []

    if text[-1] not in ['.', '?', '!']:
        return []

    formatted_text = ''
    for index in range(len(text) - 1):

        # setting sentence delimiters to '.'
        if text[index] in ['.', '?', '!'] and text[index+1] is ' ':
            formatted_text += '.'

        # leaving only characters and spaces in the sentence
        if text[index].isalpha() or text[index] is ' ':
            formatted_text += text[index]


    # splitting text into sentences
    formatted_text = formatted_text.split('.')

    # creating final list of sentences
    sentence_list = []

    for sentence in formatted_text:

        # adding sentence begin and end symbols and converting to lowercase
        sentence = '<s> '+ sentence.lower() +' </s>'

        # splitting the words and adding the sentence to the final list
        sentence_list.append(sentence.split())

    return sentence_list
