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
     
     
def propose_candidates(word: str, max_depth_permutations: int=1) -> list:
    candidates = []
    alhpabet = 'abcdefghijklmnopqrstuvwxyz'

    # удаление буквы
    for num_of_letter in range(0, len(word)):
        temp_word = word[:num_of_letter] + word[num_of_letter + 1:]
        if(candidates.count(temp_word) == 0):
            candidates.append(temp_word)

    # вставка буквы
    for num_of_letter in range(0, len(word)):
        for letter_for_change in alhpabet:
            temp_word = word[:num_of_letter] + letter_for_change + word[num_of_letter:]
            if (candidates.count(temp_word) == 0):
                candidates.append(temp_word)

    # замена буквы
    for num_of_letter in range(0, len(word)):
        for changed_letter in alhpabet:
            temp_word = word[:num_of_letter] + changed_letter + word[num_of_letter + 1:]
            if (candidates.count(temp_word) == 0):
                candidates.append(temp_word)

    # перестановка 2 соседних букв
    for num_of_letter in range(0, len(word) - 1):
        temp_word = word[:num_of_letter] + word[num_of_letter + 1] + word[num_of_letter] + word[num_of_letter + 2:]
        if (candidates.count(temp_word) == 0):
            candidates.append(temp_word)
    return candidates


def keep_known(candidates: tuple, frequencies: dict):
    candidates2 = []
    for dict_words in frequencies:
        if dict_words in candidates:
            candidates2.append(dict_words)
    return candidates2


def choose_best(frequencies: dict, candidates: tuple):
    if frequencies == None:
        return None
    
    if candidates == None:
        return None
    result_word = None
    max_num = 0
    for candidate in candidates:
        if candidate in frequencies:
            value = frequencies.get(candidate)
        else:
            value = 0
    
        if value > max_num:
            max_num = value
            result_word = candidate
    
    return result_word


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str):
    word = word.lower()
    if word in frequencies:
        return word

    if word in as_is_words:
        return word

    candidates = propose_candidates(word)
    candidates = keep_known(candidates, frequencies)
    r_word = choose_best(frequencies, candidates)
    return r_word


