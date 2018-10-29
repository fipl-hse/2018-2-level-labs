"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

def propose_candidates(word: str, max_depth_permutations: int = 1):
    if not word:
        return []
    if type(max_depth_permutations) != 1:
        return []
    if word == None:
        return []
    if word == '':
        return []

    candidates = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # deleting
    for i in range(len(word)):
        excepted = word[:i] + word[i + 1:]
        if excepted not in candidates:
            candidates.append(excepted)

    # adding
    for i in range(len(word) + 1):
        for letter in alphabet:
            add = word[:i] + letter + word[i:]
            if add not in candidates:
                candidates.append(add)

    # replacing
    for i in range(len(word)):
        for letter in alphabet:
            replace = word[:i] + letter + word[i + 1:]
            if replace not in candidates:
                candidates.append(replace)

    # shuffling
    for i in range(len(word)):
        for letter in alphabet:
            shuffle = word[:i] + letter + word[i + 1:]
            if shuffle not in candidates:
                candidates.append(shuffle)

    return candidates

def keep_known(candidates: tuple, frequencies: dict):
    if frequencies == None:
        return []
    if candidates == None:
        return []
    if type(candidates) != tuple:
        return []

    known_words = []
    for words in candidates:
        if words in frequencies:
            known_words.append(words)

    return known_words

def choose_best(frequencies: dict, candidates: tuple):
    if frequencies is None or frequencies == {} or candidates is None:
        return 'UNK'
    else:
        for cand in candidates:
            if type(cand) != str:
                list(candidates).pop(cand)
        new_dictionary = {}
        for el in frequencies.items():
            if type(el[0]) == str:
                new_dictionary[el[0]] = el[1]
        if candidates == ():
            return 'UNK'
        else:
            max_freq = []
            max_freq_key_value = []
            for value in sorted(new_dictionary.values()):
                if value == max(sorted(new_dictionary.values())):
                    max_freq.append(value)
            for el in new_dictionary.items():
                if el[1] == value:
                    max_freq_key_value.append(el)
            max_freq_key = []
            for el in max_freq_key_value:
                max_freq_key.append(el[0])
            the_best = []
            if type(candidates) != tuple:
                candidates = tuple(candidates)
            for cand in candidates:
                if cand in max_freq_key:
                    the_best.append(cand)
            selected = sorted(the_best)
            chosen = selected[0]
            return chosen

def spell_check_word(frequencies, as_is_words, word):
    if frequencies is None or word is None:
        return 'UNK'
    if as_is_words is not None and word.upper() in as_is_words:
        return word
    if word in frequencies:
        return word
    candidates = propose_candidates(word)
    familiar = keep_known(tuple(candidates), frequencies)
    checked_words = choose_best(frequencies, tuple(familiar))
    return checked_words