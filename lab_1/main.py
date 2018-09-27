"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
dict_freq1 = {}


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
    stop_words_values = []
    if stop_words = None:
        return {}

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
    list_sort = []
    list_with_keys = []
    
    if type(top_n) != int:
        return ()

    for value in final_dict.values():
        list_sort.append(list_sort)
        list_sort.sort(reverse = True)
    

    for i in list_sort:
        for key, value in final_dict.items():
            if value == i:
                list_with_keys.append(key)
                final_dict[key] = ""
                break

    if top_n > len(list_with_keys):
        return tuple(list_with_keys)
    if top_n < 0:
        return()

    max_n_words = tuple(list_with_keys[:top_n])
    return max_n_words
