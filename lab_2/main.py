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


def propose_candidates(word, max_depth_permutations: int=1) -> list:
    variations = []
    if word == '' or word is None or max_depth_permutations is None or max_depth_permutations == str(
            max_depth_permutations) \
            or not max_depth_permutations > 0:
        return variations
    else:
        for i in range(len(word) + 1):
            for a in LETTERS:
                the_word = word[:i] + a + word[i:]
                variations.append(the_word)
        for i in range(len(word)):
            variations.append(word[:i] + word[i + 1:])
            for a in LETTERS:
                new_word = word[:i] + a + word[i + 1:]
                variations.append(new_word)
        for i in range(len(word) - 1):
            variations.append(word[0:i] + word[i + 1] + word[i] + word[i + 2:])
        final_result = list(set(variations))
        return final_result


def keep_known(candidates: tuple, frequencies: dict) -> list:
    possible_words = []
    if candidates is None or frequencies is None or not candidates == tuple(candidates):
        return possible_words
    else:
        for key in frequencies.keys():
            if key in candidates:
                possible_words.append(key)
        return possible_words


def choose_best(frequencies: dict, candidates: tuple) -> str:
    needed_keys = []
    dict_value = []
    if frequencies is None or candidates is None or candidates == tuple([]) or frequencies == dict():
        return 'UNK'
    for key in list(frequencies.keys()):
        if key not in candidates:
            frequencies.pop(key)
    for value in frequencies.values():
        dict_value.append(value)
    max_value = max(dict_value)
    for key, value in frequencies.items():
        if value == max_value:
            needed_keys.append(key)
    needed_keys.sort()
    needed_word = needed_keys[0]
    return needed_word



