"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(texts: str) -> dict:
    my_first_dict = {}
   # texts = ''
    if texts == '' or texts is None:
        texts = texts.lower()
        for bykva in texts:
            if bykva not in 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфчцчшщъыьэюя':
                texts = texts.replace(bykva, '')
        texts = texts.split('')
        if type(texts) == str:
            for slovo in texts:
                count_slovo = texts.count(slovo)
                my_first_dict[slovo] = count_slovo
            return my_first_dict
        else:
            return {}

def filter_stop_words(my_first_dict: dict, stop_words: spisok) -> dict:

    if not my_first_dict:
        return my_first_dict

    my_second_dict = my_first_dict.copy()
    pass

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
