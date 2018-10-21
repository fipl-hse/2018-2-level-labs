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
    if word == None:
        return []
    candidates = []
    let = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(word)): #delete the character
        no_letter = word[:i] + word[i + 1:]
        if no_letter not in candidates:
            candidates.append(no_letter)

    for i in range(len(word)): #add the letter between the characters
        for el in let:
            add = word[:i] + el + word[i:]
            if add not in candidates:
                candidates.append(add)

    for i in range(len(word)): #replace the character with a letter
        for el in let:
            replace = word[:i] + el + word[i + 1:]
            if replace not in candidates:
                candidates.append(replace)

    for i in range(0, len(word)-1): #swap 2 characters
        swap = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        if swap not in candidates:
            candidates.append(swap)

    return candidates
 
def keep_known(candidates: tuple, frequencies: dict) -> list:
    if frequencies == None:
        return []
    if candidates == None:
        return []
    if type(candidates) != tuple:
        return []
    known_word = []
    for words in candidates:
        if words in frequencies:
            known_word.append(words)
    return known_word
 
def choose_best(frequencies: dict, candidates: tuple) -> str:
    if frequencies == None:
        return 'UNK'
    if candidates == None:
        return 'UNK'
    if frequencies == tuple([]):
        return 'UNK'
    if candidates == dict():
        return 'UNK'
    result_word = None
    times_in_dict = 0
    for i in candidates:
        if i in frequencies:
            value = frequencies.get(i)
        else:
            value = 0
          
        if value > times_in_dict:
            times_in_dict = value
            result_word = i
           
        if value == times_in_dict:
            lst = sorted(candidates)
            result_word = lst[1]

    return result_word

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
  pass
 
def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
  pass
