"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

from collections import Counter
def calculate_frequences(text: str)-> dict:
    vocabulary = {}
    if type(text) == str:
        text = text.lower()
        text_list = []
        marks_and_numbers = """['0','1','2','3','4','5','6','7','8','9','.',','!',','?',
        ':',';','\','/','"','*','-','_',''','"','@','#','$','%','^','&','(',')','+','=',
        '[',']','{','}','~','<','>','№' ]"""
        for m_n in marks_and_numbers:
            if m_n in text:
                text = text.replace(m_n, ' ')
        text_list = text.split()
        for i in text_list:
            if vocabulary.get(i):
                vocabulary[i] += 1
            else:
                vocabulary[i] = 1
    elif text is None or type(text) != str:
        return vocabulary
    return vocabulary


def filter_stop_words(vocabulary: dict, stop_words: tuple)-> dict:
    if not isinstance(vocabulary, dict):
        return {}
    if not isinstance(stop_words, tuple):
        return vocabulary
    del_list = []
    for key in vocabulary.keys():
        if key in stop_words:
            del_list.append(key)
        if not isinstance(key, str):
            del_list.append(key)
    for element in del_list:
        vocabulary.pop(element)
    return vocabulary

def get_top_n(vocabulary: dict, n_top_words: int)-> tuple:
    if n_top_words < 0:
        return ()
    v_sort = Counter(vocabulary).most_common()
    top_n = v_sort[:n_top_words]
    temp_list = []
    for temp in top_n:
        temp_list.append(temp[0])

    return tuple(temp_list)
