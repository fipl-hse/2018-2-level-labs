"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
def print_dictionary(d: dict):
    for b, d in d.items():
        print(b, d)

def calculate_frequences(text: str) -> dict:
    frequencies = {}

    if type(text) == str:
        for i in text:
            if i.isalpha():
                pass
            else:
                text = text.replace(i, ' ')
        text = text.lower()
        words = text.split(' ')
        for w in words:
            if w.isalpha():
                if w in frequencies.keys():
                    n = frequencies[w]
                    frequencies[w] = n + 1
                else:
                    frequencies[w] = 1

        return frequencies
    elif text == None or type(text) != str:
        return frequencies
    """
    Calculates number of times each word appears in the text
    """
    

frequencies = calculate_frequences(text)
print('Частотный словарь')
print_dictionary(frequencies)

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    frequencies1 = {}
    if type(stop_words) == tuple:
        dct1 = dict(frequencies)
        for k, v in dct1.items():
            if k in stop_words:
                del frequencies[k]
        return frequencies
    elif stop_words == None or stop_words !=tuple:
        return frequencies1
    """
    Removes all stop words from the given frequencies dictionary
    """ 

clear_dct = filter_stop_words(frequencies, stop_words)
print('Частотный словарь чистый')
print_dictionary(clear_dct)

def get_top_n(frequencies: dict, top_n: int) -> tuple:
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
    """
    Takes first N popular words
    """
   

print('Первые', n, 'по популярности слов')
get_top_n(frequencies, n)

