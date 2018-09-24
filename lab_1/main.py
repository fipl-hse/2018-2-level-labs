"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
from typing import Dict, Any


def calculate_frequences(text: str):
    freq_dict = {}
    if text == '' or text is None:
        return freq_dict
    text = str(text)
    lower_text = text.lower()
    for symbol in lower_text:
        if not symbol.isalpha():
            lower_text = lower_text.replace(symbol, ' ')
    list = lower_text.split()
    for word in list:
        if word.isalpha():
            dict_key = word
            dict_value = list.count(word)
            new_dict = {dict_key: dict_value}
            freq_dict.update(new_dict)
    return freq_dict


def filter_stop_words(freq_dict, stop_words):
    filtered_dict = {}
    if freq_dict is not None and stop_words is not None:
        for key, value in freq_dict.items():
            if key == str(key):
                if key not in stop_words:
                    filtered_dict.update({key: value})
    return filtered_dict


def get_top_n(filtered_dict, n) -> tuple:
    key_list = []
    new_list = []
    if n < 0:
        return ()
    for key, value in filtered_dict.items():
        key_list.append([value, key])
        sorted(key_list)
    fixed_list = key_list[: n]
    for element in fixed_list:
        needed_element = element[1]
        new_list.append(needed_element)
    dict_tuple = tuple(new_list)
    return dict_tuple

# Changed the 3rd function. Still working, thought that it might be better. This is the "before" function
# def get_top_n(filtered_dict, n) -> tuple:
#    key_list = []
#    if n > 0:
#       for key in filtered_dict.keys():
#           key_list.append(key)
#        key_list = key_list[: n]
#        dict_tuple = tuple(key_list)
#        return dict_tuple
#    else:
#        dict_tuple = ()
#        return dict_tuple
