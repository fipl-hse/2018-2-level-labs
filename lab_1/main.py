"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str):
    freq_dict = {}
    if text == '' or text is None:
        return freq_dict
    text = str(text)
    lower_text = text.lower()
    for symbol in lower_text:
        if not symbol.isalpha():
            lower_text = lower_text.replace(symbol, ' ')
    word_list = lower_text.split()
    for word in word_list:
        if word.isalpha():
            dict_key = word
            dict_value = word_list.count(word)
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


def get_top_n(filtered_dict, element_count) -> tuple:
    key_list = []
    new_list = []
    if element_count < 0:
        return ()
    for key, value in filtered_dict.items():
        key_list.append([value, key])
        sorted(key_list)
    fixed_list = key_list[: element_count]
    for element in fixed_list:
        needed_element = element[-1]
        new_list.append(needed_element)
    dict_tuple = tuple(new_list)
    return dict_tuple


def read_from_file(path_to_file, lines_limit: int) -> str:
    try:
        given_text = open(path_to_file).read()
        new_text = ''
        for line in given_text:
            if lines_limit == 0:
                break
            new_text = new_text + line
            lines_limit -= 1
        return new_text
    except IOError:
        return ()
    


def write_to_file(path_to_file: str, content: tuple):
    the_list = '\n'.join(content)
    the_file = open(path_to_file, 'w')
    the_file.write(the_list)
    the_file.close()


# Changed the whole 3rd function. Still working, just thought it might be better. This is the "before" function:
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
