"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
dict_freq1 = {}


def calculate_frequences(text: str) -> dict:

    aliens = ['.', ',', ':', '"', '`', '[', ']', '?', '!', '@', '&', "'", '-', '$', '^', '*', '(', ')', '_', '“', '”', '’', '#',
              '%', '<', '>', '*', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if type(text) != str:
            return {}

    text = text.lower()
    text_split = text.split(" ")
    text2 = []
    clean = ''
    for i in text_split:
        for symbol in i:
            if symbol.isalpha():
                text2.append(symbol)
                clean = ''
            elif symbol.isdigit():
                continue
                
    if text2 == []:
        return {}
    else:
        dict_freq1[i] = text2.count(i)
        
    return dict_freq1


def filter_stop_words(dict_freq1: dict, stop_words: tuple) -> dict:

    stop_words_values = []
    
    if stop_words == None:
        return dict_freq1
    if dict_freq1 == None:
        return {}
    else:
        dict_as_list = list(dict_freq1)
        stop_words_list = list(stop_words) 
        for i in dict_as_list:
            if type(i) != str:
                return {} 
    
    for i in stop_words:
        if type(i) != str:
            stop_words_list.remove(i)
          
    for value in dict_freq1.values():
        stop_words_values.append(value)

    for i, e in enumerate(dict_as_list):
        if e == None:
            return {}
        if e in stop_words_list:
            dict_as_list.remove(e)
            del stop_words_values[i]

    final_dict = dict(zip(dict_as_list, stop_words_values))
    return final_dict


def get_top_n(final_dict: dict, top_n: int) -> tuple:
    list_sort = []
    list_with_keys = []
    
    if top_n < 0:
        return()
    
    if type(top_n) != int:
        return ()

    for value in final_dict.values():
        list_sort.append(value)
        list_sort.sort(reverse = True)
    

    for i in list_sort:
        for key, value in final_dict.items():
            if value == i:
                list_with_keys.append(key)
                final_dict[key] = ""
                break

    if top_n > len(list_with_keys):
        return tuple(list_with_keys)

    max_n_words = tuple(list_with_keys[:top_n])
    return max_n_words
