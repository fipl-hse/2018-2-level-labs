"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    if text != None and type(text) != int:
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
        if '' in frequencies:
            frequencies.pop('')
        return frequencies
    else:
        frequencies = {}
        return frequencies


def filter_stop_words(frequencies, stop_words):
    filtered_dictionary = {}
    if stop_words == None and frequencies == None:
        return filtered_dictionary
    else:
        for key in frequencies.keys():
            if key not in stop_words:
                filtered_dictionary[key] = frequencies.get(key)
        return filtered_dictionary

def get_top_n(filtered_dictionary, top_n):
    for_keys = []
    if top_n > 0:
        for key in filtered_dictionary.keys():
            for_keys.append(key)
        for_keys = for_keys[: top_n]
        tuple_dictionary = tuple(for_keys)
    else:
        tuple_dictionary = ()
    return tuple_dictionary
