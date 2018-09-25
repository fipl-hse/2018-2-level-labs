"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
def calculate_frequences(text) -> dict:
    frequent_dict = {}
    import re
    if text and isinstance(text, str):
        prepared_text = re.findall(r'[a-z]+', text.lower())
        for element in prepared_text:
            new_word = ''
            count = 1
            for el_element in enumerate(element): # вводим дополнительный цикл, где избавляемся от лишнего "мусора"
                if el_element[1] in 'qwertyuioplkjhgfdsazxcvbnm':
                    new_word += el_element[1]
            if new_word not in frequent_dict:
                frequent_dict[new_word] = count
            else:
                new_count = frequent_dict[new_word] + 1
                frequent_dict[new_word] = new_count
    return frequent_dict

def filter_stop_words(frequent_dict, stop_words) -> dict: # Removes all stop words from the given frequencies dictionary
    new_frequent_dict = {}
    if frequent_dict and stop_words:
        for word, frequency in frequent_dict.items():
            if word not in stop_words and isinstance(word, str):
                new_frequent_dict[word] = frequency
        return new_frequent_dict
    return frequent_dict

def get_top_n(frequent_dict, top_n) -> tuple:
    words = []
    frequencies = []
    tuple_top_n = ()
    if frequent_dict and top_n:
        for word, frequency in frequent_dict.items():
            words.append(word)
            frequencies.append(frequency)
        words = sort(frequencies, words)
        for i in range(top_n):
            if i <= (len(words) - 1):
                tuple_top_n = tuple_top_n[:] + (words[i],)
    return tuple_top_n

def sort(frequencies, words):
    for j in range(len(frequencies) - 2):  # сортировка строк методом пузырька
        for i in range(len(frequencies) - j - 1):
            repository_fr = 0
            repository_words = ''
            if frequencies[i] < frequencies[i + 1]:
                repository_fr = frequencies[i]
                frequencies[i] = frequencies[i + 1]
                frequencies[i + 1] = repository_fr
                repository_words = words[i]
                words[i] = words[i + 1]
                words[i + 1] = repository_words
    return words

TEXT = '''The quick brown fox jumps over the lazy dog'''
STOPWORDS = ['the', 'lazy']
N = 2
FREQUENT_DICT = calculate_frequences(TEXT)
FREQUENT_DICT = filter_stop_words(FREQUENT_DICT, STOPWORDS)
FREQUENT_DICT = get_top_n(FREQUENT_DICT, N)
