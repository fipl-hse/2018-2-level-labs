
"""
 Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences


REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)


candidates = []


def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if word == None:
        return []
    if word == '':
        return []
    if max_depth_permutations != 1:
        return []

    for i in range(len(word)):
        word1 = word[:i] + word[i + 1:]
        if word1 not in candidates:
            candidates.append(word1)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for s in range(len(word)):
        for i in alphabet:
            word2 = word[:s] + i + word[s:]
            if word2 not in candidates:
                candidates.append(word2)

    for s in range(len(word) + 1):
        for i in alphabet:
            word3 = word[:s] + i + word[s + 1:]
            if word3 not in candidates:
                candidates.append(word3)

    for s in range(0, len(word) - 1):
        word4 = word[:s] + word[s + 1] + word[s] + word[s + 2:]
        if word4 not in candidates:
            candidates.append(word4)
    return candidates


further_candidates = []


def keep_known(candidates: tuple, frequencies: dict) -> list:
    if frequencies == None:
        return []
    if candidates == None:
        return []
    if type(candidates) != tuple:
        return []
    for key in frequencies.keys():
        if type(key) != str:
             return []

    for i in candidates:
        if i in frequencies:
            further_candidates.append(i)
    return further_candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:
    final = ''
    if candidates == None:
        return 'UNK'
    if frequencies == None:
        return 'UNK'
    if candidates == tuple([]):
        return 'UNK'
    if frequencies == dict():
        return 'UNK'
    freq = 0

    for word in candidates:
        if word in frequencies:
            val = frequencies.get(word)
        else:
            val = 0
        if val > freq:
            freq += val
            final += word
        if val == freq and freq > 0:
            sp = [final, word]
            sp.sort()
            final = str(sp[0])
    return final
   
def spell_check_word(frequencies: dict, as_is_words: tuple, word: str):
    if frequencies == None or type(frequencies) != dict:
        result = 'UNK'
    else:
        if word in frequencies:
            return word
    if word == None or type(word) != str:
        result = 'UNK'
    else:
        if word.upper() in as_is_words and type(word) == str:
            return word
    if type(as_is_words) != tuple or as_is_words == None:
        candidates = tuple(propose_candidates(word, 1))
        result = choose_best(frequencies, candidates)
    return result
