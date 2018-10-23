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
        FREQ_DICT = calculate_frequences(REFERENCE_TEXT)

def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if not isinstance(word, str) or word == '' or not isinstance(max_depth_permutations, int):
        return []
    if max_depth_permutations <= 0:
        return[]

    candidates_list = set()
    for position in range(len(word)):
        candidates = (word[:position] + word[position + 1:])
        candidates_list.add(candidates)

    for symbol in LETTERS:
        for position in range(len(word)):
            candidates = (word[:position] + symbol + word[position:])
            candidates_list.add(candidates)
            if position == 0:
                candidates = symbol + word
                candidates_list.add(candidates)

    for symbol in LETTERS:
        for position in range(len(word) + 1):
            candidates = (word[:position] + symbol + word[position + 1:])
            candidates_list.add(candidates)

    for position in range(len(word) - 1):
        candidates = (word[:position] + word[position + 1] + word[position] + word[position + 2:])
        candidates_list.add(candidates)

    return list(candidates_list)

def keep_known(candidates: tuple, frequencies: dict) -> list:
    if (not isinstance(candidates, tuple)) or (not isinstance(frequencies, dict)):
        return[]
    known_candidates = []
    for candidate in candidates:
        if candidate in frequencies:
            known_candidates.append(candidate)
    return known_candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:
    if candidates is None or frequencies is None:
        return 'UNK'
    if candidates is () or len(frequencies) == 0:
        return 'UNK'

    best_candidates_list = []
    new_freq_dict = {}

    good_candidate = ''
    for candidate in best_candidates_list:
        new_freq_dict[candidate] = frequencies[candidate]
        good_candidate = candidate

    new_list = []
    itog_list = []
 #   itog_list = 0
    for key, value in new_freq_dict.items():
        new_list.append([value, key])
        new_list.sort(reverse=True)
        for candidate in new_list:
            if candidate[0] == new_list[0][0]:
                itog_list.append(candidate[1])
            else:
                continue
  #  itog_list.sort()
    good_candidate = itog_list
    return good_candidate



#    for word in new_freq_dict_extra.keys():
  #      itog_list.append(word)

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if (not isinstance(word, str)) or (not isinstance(frequencies, dict)):
        return 'UNK'
    if word in frequencies:
        return word
    if not isinstance(as_is_words, tuple):
        pass
    else:
        if word.upper() in as_is_words:
            return word
    list_candidates = propose_candidates(word)
    list_known_candidates = keep_known(tuple(list_candidates), frequencies)
    itog_candidate = choose_best(frequencies, tuple(list_known_candidates))
    return itog_candidate
