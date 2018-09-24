"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
def print_dictionary(d: dict):
    for b, d in d.items():
        print(b, d)

def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    text = text.lower()
    words = text.split(' ')
    frequencies = {}
    for w in words:
        if w in frequencies.keys():
            n = frequencies[w]
            frequencies[w] = n+1
        else:
            frequencies[w] = 1

    return frequencies

frequencies = calculate_frequences(text)
print('Частотный словарь')
print_dictionary(frequencies)

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    dct1 = dict(frequencies)
    for k, v in dct1.items():
        if k in stop_words:
            del frequencies[k]
    return dct1

clear_dct = filter_stop_words(frequencies, stop_words)
print('Частотный словарь чистый')
print_dictionary(clear_dct)

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
   res = []
    l = list(frequencies.values())
    l.sort()
    l.reverse()
    for i in range(len(l)-top_n):
        l.pop()

    for list_el in l:
        for k,v in frequencies.items():
            if v == list_el:
                res.append(k)
                del frequencies[k]
                break

    res = tuple(res)
    print(res)
    return res

print('Первые', n, 'по популярности слов')
get_top_n(frequencies, n)

