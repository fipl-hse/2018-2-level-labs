"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text: str) -> dict:
    if type(text) == str:
       split_text = text.split(' ')
       freq_dictionary = {}
       for i in split_text:
           freq_dictionary = split_text.count(i)
            
       return freq_dictionary
    else:
       return {}

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
