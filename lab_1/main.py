"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str):
    alph = '" "abcdefghijklmnopqrstuvwxyz'
    d_freq = {}
    if text == None:
      return {}
    text = str(text)
    text = text.lower()
    for e in text:
        if e not in alph:
            text = text.replace(e, "")
    text = text.split(' ')
    for e in text:
        if e not in d_freq:
            d_freq[e] = 1
        else:
            d_freq[e] += 1
    if '' in d_freq.keys():
        d_freq.pop('')
    return d_freq


def filter_stop_words(d_freq, stop_words):
    d_freq_copy = d_freq.copy()
    if d_freq == None or stop_words == None:
        return d_freq_copy
    for e in stop_words:
        if e in d_freq_copy.keys():
            d_freq_copy.pop(e)
    return d_freq_copy


def get_top_n(frequencies, top_n):
    d_freq_copy = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    if top_n > len(d_freq_copy):
        top_n = len(d_freq_copy)
    top_n_words = tuple(d_freq_copy[i][0] for i in range(top_n))
    return top_n_words
