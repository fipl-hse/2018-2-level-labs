"""This module does blah blah."""
import collections
TEXT = '''He do subjects *prepared 34 bachelor juvenile ye oh.
He feelings rem'oving informed he as 34 ignorant we prepared.
Celebrated if remarkably especia"lly an.
Goi(ng eat set she books found met aware.'''
STOP_WORDS = ('a', 'an', 'is', 'are', 'am', 'the', 'of',
'with', 'at', 'to', 'in', 'as')
TOP_N = 3
FREQUENCIES = {}
def calculate_frequences(text: str) -> dict:
    if text is None:
        text = ''
    c_elements = collections.Counter()
    words = str(text).lower()
    restr_chars = "~$%&^@*#\"{}[]\'/\n:;!?().,<>"
    for i in restr_chars:
        if i in words:
            if i == '.':
                words = words.replace(i, ' ')
            else:
                words = words.replace(i, '')
    for k in words:
        if k.isdigit() or k == '-' and k[1:].isdigit():
            words = words.replace(k, '')
    words = words.split()
    global frequencies
    for word in words:
        c_elements[word] += 1
    frequencies = dict(c_elements)
    return frequencies

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    if frequencies is None:
        frequencies = {}
    if stop_words is None:
        stop_words = tuple()
    filtered_w = {k: frequencies[k] for k in frequencies if (k not in stop_words) and (isinstance(k, str))}
    return filtered_w

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    if top_n is None or top_n < 0 or not isinstance(top_n, int):
        top_n=0
    top_w = sorted(frequencies, key=frequencies.get, reverse=True)
    top_w = ((tuple(top_w))[0:top_n])
    return top_w
