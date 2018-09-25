"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text: str) -> dict:
    if text != None and type(text) != int:
        frequencies = {}
        new_text = text.lower()
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        clean_text = ''
        if ' ' not in text:
             clean_list = text.split(None)
             frequencies = {token: clean_list.count(token) for token in clean_list}
             return frequencies
        else:
             i = 0
             for i in range(len(new_text)):
                 if new_text[i] not in alphabet:
                     clean_text = new_text.replace(text[i], ' ')
                     new_text = clean_text
             clean_list = []
             clean_list = clean_text.split(' ')
             frequencies = {token: clean_list.count(token) for token in clean_list}
             if '' in frequencies:
                 frequencies.pop('')
             return frequencies
    else:
        frequencies = {}
        return frequencies


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    new_frequencies = {}
    if stop_words =  None:
        return new_frequencies
    else:
        for word in frequencies.keys():
            if word not in stop_words:
                new_frequencies[word] = frequencies.get(word)
        return new_frequencies


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    list_keys = []
    if n <= 0:
        tuple_top = ()
        return tuple_top
    else:
        for key in filtered_dict.keys():
            list_keys.append(key)
        slice_keys = list_keys[:n]
        tuple_top = tuple(slice_keys)
        return tuple_top

