"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def read_from_file(path_to_file: str, lines_limit: int) -> str:
    text = open(path_to_file)
    first_lines = text.readlines()[0:lines_limit]
    text.close()
    return first_lines


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if isinstance(text, str):
        if text == '' or text is None:
            freq_dict = {}
        else:
            text = text.lower()
            for letter in text:
                if letter not in 'abcdefghijklmnopqrstuvwxyz':
                    text = text.replace(letter, ' ')
            text_list = text.split()
            freq_dict = {}
            for word in text_list:
                freq_dict[word] = text_list.count(word)
    else:
        freq_dict = {}
    return freq_dict


def filter_stop_words(freq_dict: dict, STOP_WORDS: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    freq_dict_clear = {}
    if STOP_WORDS is None:
        if freq_dict is None:
            freq_dict_clear = {}
        else:
            freq_dict_clear = freq_dict.copy()
    else:
        if freq_dict is None:
            freq_dict_clear = {}
        else:
            for word in freq_dict.keys():
                if isinstance(word, str) and word not in STOP_WORDS:
                    freq_dict_clear[word] = freq_dict[word]
    return freq_dict_clear


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    frequencies_list = []
    for frequency in frequencies.values():
        frequencies_list.append(frequency)
    top_n_list = []
    if top_n <= 0:
        top_n_list = []
    else:
        for word in frequencies.keys():
            if frequencies[word] == max(frequencies_list):
                top_n_list.append(word)
                frequencies_list.remove(max(frequencies_list))
    top_n_tuple = tuple(top_n_list[:top_n])
    return top_n_tuple


def write_to_file(path_to_file: str, content: tuple):
    report = open(path_to_file, 'w')
    for word in content:
        report.write(word)
        report.write('\n')
    report.close()
