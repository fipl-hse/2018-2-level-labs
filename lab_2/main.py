"""
Labour work #2
 Check spelling of words in the given  text
"""
import string
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)


def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:

    if word == '' or word is None:
        return []
    if not (isinstace(max_depth_permutations, int) or max_depth_permutations < 1:
        return []

    word = word.lower()
    candidates = []
    candidate = ''
    pos = 1

    for i in word:
        candidate = word[0:pos - 1] + word[pos:]
        candidates.append(candidate)
        pos += 1

    for letter in string.ascii_lowercase:
        pos = 0
        for i in word:
            candidate = word[0:pos] + letter + word[pos:]
            candidates.append(candidate)
            pos += 1
        candidate = word + letter
        candidates.append(candidate)

    for letter in string.ascii_lowercase:
        pos = 0
        for i in word:
            candidate = word[0:pos] + letter + word[pos + 1:len(word)]
            candidates.append(candidate)
            pos += 1
        pos = 0
    for letter in word[:len(word) - 1]:
        candidate = word
        candidate = candidate[:pos] + candidate[pos + 1] + candidate[pos + 1:]
        candidate = candidate[:pos + 1] + letter + candidate[pos + 2:]
        pos += 1
        candidates.append(candidate)

    return list(set(candidates))


def keep_known(candidates: tuple, frequencies: dict) -> list:
    if not isinstance(candidates, tuple) or candidates is None or candidates == ():
        return []
    if not isinstance(frequencies, dict) or frequencies is None or frequencies == {}:
        return []

    new_candidates = []
    for candidate in candidates:
        if frequencies.get(candidate):
            new_candidates.append(candidate)
    return new_candidates


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if not isinstance(candidates, tuple) or candidates is None or candidates == ():
        return 'UNK'
    if not isinstance(frequencies, dict) or frequencies is None or frequencies == {}:
        return 'UNK'

    for candidate in candidates:
        if isinstance(candidate, str):
            cur_candidate = candidate

    sorted(frequencies, key=lambda x: str(x))
    for candidate in candidates:
        if isinstance(candidate, str):
            if frequencies.get(candidate) is not None and frequencies.get(candidate, 0) > \
                    frequencies.get(cur_candidate, 0):
                cur_candidate = candidate
    return cur_candidate


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if not isinstance(frequencies, dict):
        return 'UNK'

    if isinstance(as_is_words, tuple):
        for i in as_is_words:

            if isinstance(i, str) and i.lower() == word:
                return word

        if frequencies.get(word) is not None:
            return word
    candidates = propose_candidates(word)
    candidates = keep_known(tuple(candidates), frequencies)
    return choose_best(frequencies, tuple(candidates))
