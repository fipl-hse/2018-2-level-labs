"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text_one: str) -> dict:
    if text_one is None or str(text_one).isdigit():
        freq_dict = {}
        return freq_dict
    for element in text_one:
        if element in """1234567890!@#$%^&*()_-=+[]{}"'/?.,<>;:`~№\n""":
            text_one = text_one.replace(element, ' ')
            continue

    text_one = text_one.lower()
    text_one = text_one.split(' ')

    freq_dict = {}
    for word_one in text_one:
        if word_one:
            frequency_word = text_one.count(word_one)
            freq_dict[word_one] = frequency_word
            continue

    return freq_dict

def filter_stop_words(frequencies_dict: dict, stop_words: tuple) -> dict:
    if stop_words is None or frequencies_dict is None:
        return frequencies_dict
    for key in list(frequencies_dict):
        if str(key).isdigit() or key in stop_words:
            frequencies_dict.pop(key)
            continue
    return frequencies_dict

def get_top_n(frequencies_dict_new: dict, top_n: int) -> tuple:

    list_of_words = []
    itog_res = []
    count = 0
    if top_n < 0:
        return ()
    for key, value in frequencies_dict_new.items():
        list_of_words.append([value, key])
    sorted(list_of_words)
    for item in list_of_words:
        if count == top_n:
            break
        itog_res.append(item[1])
        count += 1
    return tuple(itog_res)

