"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
def calculate_frequences(texts: str) -> dict:
    my_first_dict = {}
    bykva = ''
    texts_list = []

    if texts == '' or texts is None or type(texts) != str:
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

def filter_stop_words(my_first_dict: dict, stop_words: spisok) -> dict:

    if not my_first_dict:
        return my_first_dict

    my_second_dict = my_first_dict.copy()

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
