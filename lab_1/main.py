"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    text = text.lower()
    alphabet = 'qazwsxedcrfvtgbyhnujmikolp'
    clean_text = ''
    i = 0
    for i in range(len(text)):
        if text[i] not in alphabet:
            clean_text = text.replace(text[i], ' ')
            text = clean_text
    splitted_text = text.split(' ')
    frequencies = {word: splitted_text.count(word) for word in splitted_text}
    frequencies.pop('')
    return frequencies

def filter_stop_words(frequencies, stop_words):
    filtered_dictionary = {}
    for key in frequencies.keys():
        if key not in stop_words:
            filtered_dictionary[key] = frequencies.get(key)
    return filtered_dictionary


def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
