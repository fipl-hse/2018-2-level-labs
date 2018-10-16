"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences


def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    # Checking if the args are correct
    if (
        type(word) is not str or
        word is '' or
        type(max_depth_permutations) is not int
    ):
        return []
    try:
        if max_depth_permutations <= 0:
            return []
    except TypeError:
        return []

    candidates_list = set()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    len_of_word = len(word)

    for syllable_i in range(len_of_word):
        candidate = (word[:syllable_i] +
                     word[syllable_i + 1:])
        candidates_list.add(candidate)

    for alphabet_symbol in alphabet:
        for syllable_i in range(len_of_word):
            if syllable_i == 0:
                candidate = alphabet_symbol + word
                candidates_list.add(candidate)
            candidate = (word[:syllable_i] +
                         alphabet_symbol +
                         word[syllable_i:])
            candidates_list.add(candidate)

    for alphabet_symbol in alphabet:
        for syllable_i in range(len_of_word + 1):
            candidate = (word[:syllable_i] +
                         alphabet_symbol +
                         word[syllable_i + 1:])
            candidates_list.add(candidate)

    for syllable_i in range(len_of_word - 1):
        candidate = (word[:syllable_i] +
                     word[syllable_i + 1] +
                     word[syllable_i] +
                     word[syllable_i + 2:])
        candidates_list.add(candidate)
    return list(candidates_list)


def keep_known(candidates: list, as_is_words: tuple, frequencies: dict) -> list:
    future_candidates = set()
    as_is_words_new = []

    # Checking if the args are correct
    if (
        type(candidates) is not tuple or
        type(as_is_words) is not tuple or
        type(frequencies) is not dict
    ):
        return []

    for element in as_is_words:
        element = str(element).lower()
        as_is_words_new.append(element)

    for word in candidates:
        if word in as_is_words_new or word in frequencies.keys():
            future_candidates.add(word)
    return list(future_candidates)


def choose_best(frequencies: dict, candidates: list) -> str:
    list_of_value_key = []
    list_of_words = []
    new_freq_dict = {}

    if (
        type(frequencies) is not dict or
        type(candidates) is not tuple
    ):
        return 'UNK'
    if len(candidates) <= 0 or len(frequencies) <= 0:
        return 'UNK'

    for element in candidates:
        if type(element) is not str:
            continue
        if element in frequencies:
            list_of_words.append(element)

    if len(list_of_words) == 0:
        return 'UNK'

    for word in list_of_words:
        new_freq_dict[word] = frequencies[word]
    for key, value in new_freq_dict.items():
        list_of_value_key.append([value, key])
    list_of_value_key.sort(reverse=True)

    return list_of_value_key[0][1]


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word in frequencies.keys():
        return word
    first_list_of_candidates = propose_candidates(word, 1)
    second_list_of_candidates = keep_known(first_list_of_candidates, as_is_words, frequencies)
    new_word = choose_best(frequencies, second_list_of_candidates)
    return new_word


if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

