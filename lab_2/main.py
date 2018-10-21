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
    let = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(text)): #delete the character
        no_letter = text[:i]+text[i+1:]
        if no_letter not in candidates:
            candidates.append(no_letter)

    for i in range(len(text)): #add the letter between the characters
        for el in let:
            add = text[:i] + el + text[i:]
            if add not in candidates:
                candidates.append(add)

    for i in range(len(text)): #replace the character with a letter
        for el in let:
            replace = text[:i]+el+text[i+1:]
            if replace not in candidates:
                candidates.append(replace)

    for i in range(0, len(text)-1): #swap 2 characters
        swap = text[:i] + text[i + 1] + text[i] + text[i + 2:]
        if swap not in candidates:
            candidates.append(swap)

    return candidates
 
def keep_known(candidates: tuple, frequencies: dict) -> list:
  pass
 
def choose_best(frequencies: dict, candidates: tuple) -> str:
  pass

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
  pass
 
def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
  pass
