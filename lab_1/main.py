"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    dict = {}
    if isinstance(text,str):

        new_text = text.lower()
        punctuation = "~$%&^@*#1234567890\"{}[]\'/\n:;!?().,<>"

        for symb in punctuation:
            new_text = new_text.replace(symb, "")

        new_text1 = new_text.split()

        for i in range (0,len(new_text1)):
            dict[new_text1[i]] = new_text1.count(new_text1[i])

    return dict



def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    sorted_words = {}

    if not stop_words:
        stop_words = tuple()
    if frequencies:
        sorted_words = {k: frequencies[k] for k in frequencies if (k not in stop_words) and (type(k) is str)}

    return sorted_words



def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """

    sorted_list = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    if top_n > len(sorted_list):
        top_n = len(sorted_list)
    top_n_words = tuple(sorted_list[i][0] for i in range (top_n))
    return top_n_words
