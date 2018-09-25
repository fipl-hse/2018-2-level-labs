"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
dict_freq1 = {}
final_dict = {}


def calculate_frequences(text: str) -> dict:

    if type(text) != str:
        return {}

    text = text.lower()
    text_split = text.split(" ")
    text2 = []
    clean = ''

    for i in text_split:
        for symbol in i:
            if symbol.isalpha():
                clean += symbol
        if clean != '':
            text2.append(clean)
            clean = ''

    for i in text2:
        dict_freq1[i] = text2.count(i)
    return dict_freq1


def filter_stop_words(final_dict: dict, stop_words: tuple) -> dict:
  
  filtered_words = {}
  stop_words_values = []
  dict_as_list = []
  stop_words = []

    for i in stop_words:
        if type(i) != str:
            stop_words.remove(i)

    dict_as_list = list(dict_freq1)

    for value in dict_freq1.values():
        stop_words_values.append(value)

    for i, e in enumerate(dict_as_list):
        if e in stop_words:
            dict_as_list.remove(e)
            del stop_words_values[i]

    final_dict = dict(zip(dict_as_list, stop_words_values))
    return final_dict


def get_top_n(final_dict: dict, top_n: int) -> tuple:
  values = []
  list_with_keys = []
  max_n_words = []

    if type(top_n) != int:
        return ()

    for value in final_dict.values():
        values.append(value)
        values.sort(reserve = True)
    

    for i in values:
        for key, value in final_dict.items():
            if value == i:
                list_with_keys.append(key)
                final_dict[key] = ""
                break

    if top_n > len(value):
        return tuple(value)
    if top_n < 0:
        return()

    max_n_words = tuple(list_with_keys[:top_n])
    return max_n_words
