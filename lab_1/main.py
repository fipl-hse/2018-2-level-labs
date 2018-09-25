"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences() -> dict:
    """
    Calculates number of times each word appears in the text
    """
    return {'abc': 'letters'}


def calculate_frequences(my_text):

    if my_text == None or str(my_text).isdigit() or my_text == "":
        return {}

    garbage = '''!@/#$%^~,&*'.()_-+`=-0987654321"';:'''
    freq = {}
    my_text = my_text.lower()


    for c in my_text:
        if c in garbage and c in my_text:
            my_text = my_text.replace(c,'')
    t_split = my_text.split()
    for i in t_split:
        number = t_split.count(i)
        freq[i] = number
    return freq

def filter_stop_words() -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    d = {}

def filter_stop_words(freq, STOP_WORDS):

    freq_2 = freq.copy()

    if STOP_WORDS == None:
        return freq_2

    if freq == None:
        return {}

    for i in STOP_WORDS:
        if type(i) != str:
            STOP_WORDS.remove(i)

    for key in freq.keys():
        if type(key) != str:
            freq_2.pop(key)

    for c in list(freq_2):
        for i in STOP_WORDS:
            if c == i:
                freq_2.pop(c)
    return freq_2

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    d = {}

def get_top_n(freq_2, top_n):

    if top_n <= 0:
        return()


    netuple = sorted(freq_2, key=freq_2.get, reverse=True) #key - параметр сортировки, get сортирует словарь по праметру, который определяется значением
    for key in freq_2.keys():
        netuple.append(key)
    return tuple(netuple[:top_n])

top_n = 3
