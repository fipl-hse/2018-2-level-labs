"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
from builtins import str


def calculate_frequences(texts: str) -> dict:
    my_first_dict = {}
    bykva = ''
    texts_list = []

    if texts == '' or texts == None or type(texts) != str:
        return {}
    if type(texts) == str:
        texts = texts.lower()

        for bykva in texts:
            if bykva not in 'abcdefghijklmnopqrstuvwxyz':
                texts = texts.replace(bykva, '')
            if texts.isdigit():
                continue
            if bykva in 'abcdefghijklmnopqrstuvwxyz':
                texts_list.append(bykva)

        texts = texts.split('')

        for bykva in texts_list:
            my_first_dict[bykva] = texts_list.count(bykva)
            return my_first_dict
        else:
            return {}


def filter_stop_words(my_first_dict: dict, STOP_WORDS: tuple) -> dict:

    if my_first_dict == None:
        return {}
    if STOP_WORDS == None
        return {}

    my_second_dict = my_first_dict.copy()

    for new_stop_word in STOP_WORDS:
        if new_stop_word in my_second_dict:
            my_second_dict.pop(new_stop_word)
    for key in my_second_dict.keys():
        if type(key) == str and key not in STOP_WORDS:
            my_second_dict[key] = my_first_dict[key]
    return my_second_dict


def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
