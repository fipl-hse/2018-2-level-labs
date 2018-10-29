"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''


def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if (not isinstance(word, str) or
            not isinstance(max_depth_permutations, int) or word is ''):
        return []
    if max_depth_permutations <= 0:
        return []

    candidates_list = set()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    len_of_word = len(word)

    for symbol in range(len_of_word):
        candidate = (word[:symbol] + word[symbol + 1:])
        candidates_list.add(candidate)

    for alphabet_symbol in letters:
        for symbol in range(len_of_word+1):
            candidate = (word[:symbol] + alphabet_symbol + word[symbol:])
            candidates_list.add(candidate)

    for alphabet_symbol in letters:
        for symbol in range(len_of_word ):
            candidate = (word[:symbol] + alphabet_symbol + word[symbol + 1:])
            candidates_list.add(candidate)

    for symbol in range(len_of_word - 1):
        candidate = (word[:symbol] + word[symbol + 1] + word[symbol] + word[symbol + 2:])
        candidates_list.add(candidate)
    return list(candidates_list)


def keep_known(candidates: tuple, frequencies: dict) -> list:
    if (not isinstance(candidates, tuple)) or (not isinstance(frequencies, dict)):
        return []

    certain_candidates = []

    for word in candidates:
        if word in frequencies:
            certain_candidates.append(word)


    return certain_candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:
    if (not isinstance(frequencies, dict)) or (not isinstance(candidates, tuple)):
        return 'UNK'
    if candidates is () or len(frequencies) <= 0:
        return 'UNK'

    list_of_value_key = []
    list_of_words = []
    final_list = []
    new_freq_dict = {}

    list_of_words = keep_known(candidates, frequencies)

    if list_of_words is []:
        return 'UNK'

    for word in list_of_words:
        new_freq_dict[word] = frequencies[word]

    for key, value in new_freq_dict.items():
        list_of_value_key.append([value, key])

    list_of_value_key.sort(reverse=True)

    for pair in list_of_value_key:
        if pair[0] == list_of_value_key[0][0]:
            final_list.append(pair[1])
        else:
            continue

    final_list.sort()

    right_word = final_list[0]
    return right_word


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:

    if (not isinstance(frequencies, dict)) or (not isinstance(word, str)):
        return 'UNK'
    if not isinstance(as_is_words, tuple):
        pass
    else:
        if word.upper() in as_is_words:
            return word

    if word in frequencies:
        return word


    first_list_of_candidates = propose_candidates(word, 1)
    second_list_of_candidates = keep_known(tuple(first_list_of_candidates), frequencies)
    new_word = choose_best(frequencies, tuple(second_list_of_candidates))
    return new_word


if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)
