"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    text = None
    if text != None and type(text) != int:
        frequencies = {}
        new_text = text.lower()
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        clean_text = ''
        if ' ' not in text:
             clean_list = text.split(None)
             frequencies = {token: clean_list.count(token) for token in clean_list}
             return frequencies
        else:
             i = 0
             for i in range(len(new_text)):
                 if new_text[i] not in alphabet:
                     clean_text = new_text.replace(text[i], ' ')
                     new_text = clean_text
             clean_list = []
             clean_list = clean_text.split(' ')
             frequencies = {token: clean_list.count(token) for token in clean_list}
             if '' in frequencies:
                 frequencies.pop('')
             return frequencies
    else:
        frequencies = {}
        return frequencies




def filter_stop_words(frequencies, stop_words):
    new_frequencies = {}
    stop_words = ()
    for word in frequencies.keys():
        if word not in stop_words:
            new_frequencies[word] = frequencies.get(word)
    print(new_frequencies)
    return new_frequencies


filter_stop_words()

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
