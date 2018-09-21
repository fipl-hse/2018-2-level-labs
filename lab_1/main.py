import re

def calculate_frequences(text) -> dict:
    text = re.sub(r'[^\w\s]+|[\d]+','',text)
    if text == '':
        print ({})
    else:
        text = text.lower()
        text = text.split(' ')
        frequency = {}
        for i in text:
            if i not in frequency:
                frequency[i] = 1
            else:
                num = frequency.get(i)
                frequency[i] = num+1
        print (frequency)
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
    print (frequency)
    pass

def get_top_n() -> tuple:
    freq = list(frequency.items())
    freq_sort = sorted(freq, key=lambda x: x[1], reverse = True)
    top_n = max(freq_sort, key=lambda x: x[1])[0]
    print (top_n)
    pass
