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

    def put(self, word:str) -> int:
        id = 1
        if word and isinstance(word, str):
            if word not in self.storage.keys():
                if self.storage:
                    id = max(self.storage.values()) + 1
                    self.storage[word] = id
                else:
                    self.storage[word] = id
            return self.storage[word]
        else:
            return self.storage

    def get_id_of(self, word: str) -> int:
        if word in self.storage.keys():
            return self.storage[word]
        else:
            return -1

    def get_original_by(self, id: int) -> str:
        if id in self.storage.values():
            for word in self.storage.keys():
                if id == self.storage[word]:
                    return word
        else:
            return 'UNK'

    def from_corpus(self, corpus: tuple):
        if corpus and ' ' not in corpus:
            if corpus[0] != '<s>':
                for sentence in corpus:
                    for word in sentence:
                        WordStorage.put(self, word)
            else:
                for word in corpus:
                    WordStorage.put(self, word)
        else:
            return {}


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence and isinstance(sentence, tuple):
            for index in range(len(sentence) - 2):
                three_gram = (sentence[index], sentence[index + 1], sentence[index + 2])
                if three_gram not in self.gram_frequencies.keys():
                    self.gram_frequencies[three_gram] = 1
                else:
                    present_value = self.gram_frequencies[three_gram]
                    self.gram_frequencies[three_gram] = present_value + 1
            return 'OK'
        else:
            return 'ERROR'

    def calculate_log_probabilities(self):
        import math
        for three_gram in self.gram_frequencies.keys():
            first_word = three_gram[0]
            second_word = three_gram[1]
            denominator = 0
            for three_gram_2 in self.gram_frequencies.keys():
                if three_gram_2[0] == first_word and three_gram_2[1] == second_word:
                    denominator += self.gram_frequencies[three_gram_2]
            numerator = self.gram_frequencies[three_gram]
            if denominator > 0 and len(self.gram_frequencies.keys()) >= 2:
                log_probability = math.log(numerator / denominator)
            else:
                log_probability = 0.0
            self.gram_log_probabilities[three_gram] = log_probability

    def get_three_gram_by_probability(self, probability: int, dictionary: dict) -> tuple:
        if probability in dictionary.values():
            for three_gram in dictionary.keys():
                if probability == dictionary[three_gram]:
                    return three_gram
        else:
            return 'UNK'

    def helper_for_prediction(self, prefix: tuple) -> tuple: #ищет максимальную вероятность из би-граммов вида (<число из префикса>, <что найдется в словаре>)
        current_dict = {}
        for three_gram in self.gram_log_probabilities.keys():
            if three_gram[0] == prefix[0] and three_gram[1] == prefix[1]:
                current_dict[three_gram] = self.gram_log_probabilities[three_gram]
        if current_dict:
            probability_of_most_probable_three_gram = max(current_dict.values())
        else:
            probability_of_most_probable_three_gram = 0
        result = NGramTrie.get_three_gram_by_probability(self, probability_of_most_probable_three_gram, current_dict)
        return result

    def predict_next_sentence(self, prefix: tuple) -> list:
        import re
        result = []
        if prefix and isinstance(prefix, tuple):
            if len(prefix) == 2:
                result += prefix
                str_of_three_grams = ''
                for three_gram in self.gram_log_probabilities.keys():
                    str_of_three_grams += str(three_gram)
                    str_of_three_grams += ' '
                while re.search(str(prefix), str_of_three_grams):
                    next_word = NGramTrie.helper_for_prediction(self, prefix)
                    if next_word != 'UNK':
                        result.append(next_word[2])
                        prefix = (next_word[1], next_word[2],)
                    else:
                        break
        return result

       
def encode(storage_instance, corpus) -> list:
    id_matrix_of_sentences = []
    if storage_instance and corpus and ' ' not in corpus:
        if corpus[0] != '<s>':
            for sentence in corpus:
                id_sentence = []
                for word in sentence:
                    id_sentence.append(WordStorage.get_id_of(self, word))
                id_matrix_of_sentences.append(sentence)
        else:
            for word in corpus:
                id_matrix_of_sentences.append(WordStorage.get_id_of(self, word))
    return id_matrix_of_sentences
   
   
def split_by_sentence(text: str) -> list:
    matrix_of_sentences = []
    if text and isinstance(text, str) and ('.' in text or '?' in text or '!' in text) and ' ' in text:
        import re
        result = re.split(r'[.!?]', text)
        reresult = result[:-1]#избавляемся от лишних пробелов и пустоты в конце
        number_of_sentences = len(reresult)
        for i in range(number_of_sentences):
            sentence = ['<s>', ]
            prepared_text = reresult[i].lower().split(' ')
            for element in prepared_text:
                new_word = ''
                for el_element in enumerate(element):  # вводим дополнительный цикл, где избавляемся от лишнего "мусора"
                    if el_element[1] in 'qwertyuioplkjhgfdsazxcvbnm':
                        new_word += el_element[1]
                if new_word:
                    sentence.append(new_word)
            sentence.append('</s>')
            matrix_of_sentences.append(sentence)
    return matrix_of_sentences
