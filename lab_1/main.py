import re

text = input('')
stop_words = input('')


def calculate_frequences(text) -> dict:
    text_wos = re.sub(r'[^\w\s]+|[\d]+', '', text)
    text_l = text_wos.lower()
    if text_l == '':
        print({})
    else:
        text_split = text_l.split(' ')
        frequency = {}
        for i in text_split:
            if i not in frequency:
                frequency[i] = 1
            else:
                num = frequency.get(i)
                frequency[i] = num+1
        if '' in frequency:
            del frequency['']
         return frequency
        filter_stop_words(frequency, stop_words)
        get_top_n()
    pass


def filter_stop_words(frequency, stop_words) -> dict:
    stop_words = stop_words.lower()
    stop_words = stop_words.split(', ')
    frequency_copy = frequency.copy()
    for i in frequency_copy:
        for n in stop_words:
            if i == n:
                del frequency[i]
    return frequency
    pass


def get_top_n() -> tuple:
    result = collections.Counter(frequency).most_common(top_n)
    i = 0
    top = []
    while i < top_n or i != len(result):
        top.append(max(result, key=lambda x: x[1])[0])
        result.remove(max(result, key=lambda x: x[1]))
        i += 1
    top_tuple = tuple(top)
    return top_tuple
    pass
