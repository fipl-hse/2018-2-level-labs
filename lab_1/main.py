"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
from typing import Dict, Any


def calculate_frequences(text: str):
    freq_dict = {}
    if text == '' or text is None:
        return freq_dict
    else:
        text = str(text)
        lower_text = text.lower()
        for symbol in lower_text:
            if not symbol.isalpha():
                fixed_text = lower_text.replace(symbol, ' ')
                lower_text = fixed_text
        list = lower_text.split()
        for word in list:
            if word.isalpha():
                dict_key = word
                dict_value = list.count(word)
                new_dict = {dict_key: dict_value}
                freq_dict.update(new_dict)
        return freq_dict


def filter_stop_words(freq_dict, STOP_WORDS):
    filtered_dict = {}
    if freq_dict is not None and STOP_WORDS is not None:
        for key, value in freq_dict.items():
            if key not in STOP_WORDS:

                filtered_dict.update({key: value})
    return filtered_dict

            



def get_top_n(filtered_dict, n) -> tuple:
    key_list = []
    if n > 0:
        for key in filtered_dict.keys():
            key_list.append(key)
        key_list = key_list[: n]
        dict_tuple = tuple(key_list)
        return dict_tuple
    else:
        dict_tuple = ()
        return dict_tuple
