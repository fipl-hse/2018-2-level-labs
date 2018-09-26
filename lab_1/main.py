import re
from string import punctuation
from collections import Counter
r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
text = '''He do subjects prepared 34 bachelor juvenile ye oh.
He feelings removing informed he as 34 ignorant we prepared.
Celebrated if remarkably especially an.
Going eat set she books found met aware.'''
stop_words = ('a', 'an', 'is', 'are', 'am', 'the', 'of',
'with', 'at', 'to', 'in', 'as')
top_n = 3
def calculate_frequences(text: str) -> dict:
    if text is None:
        pass
    words = str(text).lower()
    words = r.split(words)
    global frequencies
    frequencies = Counter(words).most_common()
    frequencies = dict(frequencies)
    if frequencies is None:
        frequencies = {}
    return frequencies

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    if stop_words is None:
        stop_words = tuple()
        
    filtered_w = {k: frequencies[k] for k in frequencies if (k not in stop_words) and
                  (type(k) is str) and (not k.isdigit() or k == '-' and k[1:].isdigit())}
    return filtered_w

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    if top_n is None:
        pass
    top_w = list(frequencies.items())
    top_w = ((tuple(top_w))[0:top_n])
    return top_w
    
