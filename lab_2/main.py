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

def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if word is None or word == '':
        return []

    if max_depth_permutations != 1:
        return []
    candidates = []
    alhpabet = 'abcdefghijklmnopqrstuvwxyz'

    # удаление буквы
    for num_of_letter in range(0, len(word)):
        temp_word = word[:num_of_letter] + word[num_of_letter + 1:]
        if candidates.count(temp_word) == 0:
            candidates.append(temp_word)

    # вставка буквы
    for num_of_letter in range(0, len(word)+1):
        for letter_for_change in alhpabet:
            temp_word = word[:num_of_letter] + letter_for_change + word[num_of_letter:]
            if candidates.count(temp_word) == 0:
                candidates.append(temp_word)

    # замена буквы
    for num_of_letter in range(0, len(word)):
        for changed_letter in alhpabet:
            temp_word = word[:num_of_letter] + changed_letter + word[num_of_letter + 1:]
            if candidates.count(temp_word) == 0:
                candidates.append(temp_word)

    # перестановка 2 соседних букв
    for num_of_letter in range(0, len(word) - 1):
        temp_word = word[:num_of_letter] + word[num_of_letter + 1] + word[num_of_letter] + word[num_of_letter + 2:]
        if candidates.count(temp_word) == 0:
            candidates.append(temp_word)
    return candidates

def keep_known(candidates: tuple, frequencies: dict):
    if candidates is None:
        return []
    if frequencies is None:
        return []
    if isinstance(candidates, tuple) is False:#####
        return []
    candidates2 = []
    for dict_words in frequencies:
        if dict_words in candidates:
            candidates2.append(dict_words)
    return candidates2


def choose_best(frequencies: dict, candidates: tuple):
    if frequencies is None:
        return 'UNK'
    if candidates == None:
        return 'UNK'
    if candidates == ():
        return 'UNK'
    if frequencies == dict():
        return 'UNK'
    result_word = ''
    max_num = 0
    for candidate in candidates:
        if candidate in frequencies:
            value = frequencies.get(candidate)
        else:
            value = 0

        if value > max_num:
            max_num = value
            result_word = candidate
 
        if value == max_num and max_num > 0:
            temp_list = [result_word, candidate]
            temp_list.sort()
            result_word = temp_list[0]
    return result_word

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str):
    if frequencies is None:
        return 'UNK'
    if word is None:
        return 'UNK'

    word = word.lower()
    if word in frequencies:
        return word
    if type(as_is_words) == tuple:
        if word in as_is_words:
            return word
        word = word.upper()#
        if word in as_is_words:#
            word = word.lower()#
            return word#
    word = word.lower()

    candidates = tuple(propose_candidates(word))
    candidates1 = tuple(keep_known(candidates, frequencies))
    r_word = choose_best(frequencies, candidates1)#+tuple
    return r_word
