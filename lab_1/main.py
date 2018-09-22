"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if type(text) is str:
        if text == '' or text is None:
            freq_dict = {}
        else:
            text = text.lower()
            for letter in text:
                if letter not in 'abcdefghijklmnopqrstuvwxyz':
                    text = text.replace(letter, ' ')
            text_list = text.split()
            freq_dict = {}
            for word in text_list:
                freq_dict[word] = text_list.count(word)
    else:
        freq_dict = {}
    return freq_dict
    pass

def filter_stop_words() -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    pass

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
