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


def propose_candidates(word: str, max_depth_permutations: int=1) -> list:

    # if data is correct
    if word == '' or word is None or not isinstance(word, str):
        return []
    if not isinstance(max_depth_permutations, int):
        return []
    if max_depth_permutations != 1:
        return []

    lst_of_candidates = []
    len_of_word = len(word)
    abc = 'qwertyuiopasdfghjklzxcvbnm'

    # removing 1 letter
    for letter in range(len_of_word):
        '''candidate = (word[:letter] + word[letter + 1:])
        lst_of_candidates.append(candidate)'''

        left_part_word = word[:letter]
        right_part_word = word[letter + 1:]
        candidate = left_part_word + right_part_word
        lst_of_candidates.append(candidate)

    # adding 1 letter
    for alpha in abc:
        for i in range(len_of_word):
            if i == 0:
                candidate = alpha + word
                lst_of_candidates.append(candidate)
            candidate = (word[:i] + alpha + word[i:])
            lst_of_candidates.append(candidate)

    # replacing 1 letter
    for alpha in abc:
        for el in range(len_of_word + 1):
            candidate = (word[:el] + alpha + word[el + 1:])
            lst_of_candidates.append(candidate)

    # exchanging 2 close letters
    for place in range(1, len_of_word):
        left_part_word = word[:place - 1] + word[place]
        right_part_word = word[place - 1] + word[place + 1:]
        candidate = left_part_word + right_part_word
        lst_of_candidates.append(candidate)

    unique_candidates = set(lst_of_candidates)
    lst_of_candidates = list(unique_candidates)
    return lst_of_candidates


def keep_known(candidates: tuple, frequencies: dict) -> list:

    # if data is correct
    if not candidates or not frequencies:
        return []
    if not isinstance(frequencies, dict) or not isinstance(candidates, tuple):
        return []

    frequencies_checked = {}
    for key, value in frequencies.items():
        if isinstance(key, str):
            frequencies_checked[key] = value

    new_candidates = []
    for candidate in candidates:
        if candidate in frequencies_checked and isinstance(candidate, str):
            new_candidates.append(candidate)

    return new_candidates


def choose_best(frequencies: dict, candidates: tuple) -> str:

    # if data is correct

    if not candidates or isinstance(candidates, str):
        return 'UNK'
    if candidates is None or frequencies is None:
        return 'UNK'

    candidates_checked = []
    for candidate in candidates:
        if isinstance(candidate, str):
            candidates_checked.append(candidate)

    if len(frequencies) == 0:
        return 'UNK'

    frequencies_checked = {}
    for key, value in frequencies.items():
        if isinstance(key, str):
            frequencies_checked[key] = value

    # exploring frequencies_checked to find the most frequent one

    lst_of_freqs = list(frequencies_checked.values())

    max_freq = max(lst_of_freqs)
    words_with_equal_freqs = []

    for word, freq in frequencies_checked.items():
        if freq == max_freq:
            words_with_equal_freqs.append(word)

    words_with_equal_freqs.sort()

    best_word = words_with_equal_freqs[0]
    return best_word


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:

    # if data is correct
    if frequencies is None or word is None:
        return 'UNK'
    if as_is_words is not None and word.upper() in as_is_words:
        return word

    if word in frequencies:
        return word

    candidates = propose_candidates(word)
    new_candidates = keep_known(tuple(candidates), frequencies)
    best_word = choose_best(frequencies, tuple(new_candidates))

    return best_word
