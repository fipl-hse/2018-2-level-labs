"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
import re

def calculate_frequences(text) -> dict:
    
    text = re.sub(r'[^\w\s]+|[\d]+', '', text)
    if text = '':
        print ({})
    else:
        text = text.lower()
        text = text.split(' ')
        frequency = {}
        for i in text:
            if i not in frequency:
                if i != '':
                    frequency[i] = 1
            else:
                num = frequency.get(i)
                frequency[i] = num+1
        filter_stop_words(frequency, stop_words)
        get_top_n(frequency, top_n)
        
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
