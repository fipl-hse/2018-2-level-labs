"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
dict_freq1 = {}
final_dict = {}


def calculate_frequences(text: str) -> dict:
    aliens = ['.', ',', ':', '"', '`', '[', ']', '?', '!', '@', '&', "'", '-', '$', '^', '*', '(', ')', '_', '“', '”',
              '’', '#', '%', '<', '\n', '"', '>', '*', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if type(text) != str:
        return {}

    for i in text:
        for i in aliens:
            text = text.replace(i, '')

    text = text.lower()
    text_split = text.split(' ')
    while '' in text_split:
        text_split.remove('')

    if text == []:
        return {}
    else:
        for i in text_split:
            dict_freq1[i] = text_split.count(i)

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

    if final_dict.keys():
        if key != str:
            return ()

    if top_n < 0:
        return ()

    if type(top_n) != int:
        return ()

    for value in final_dict.values():
        list_sort.append(value)
        list_sort.sort(reverse=True)

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



text = """Th0e " lazy quick, quick 7brown \n
                f:ox jumps \n
               o*ver t77he quick lazy \n
                $^dog quick&"""


a = calculate_frequences(text)
b = filter_stop_words(dict_freq1,('fox', 'dog', 'the',))
c = get_top_n(final_dict, 2)
print(a)
print(b)
print(c)
