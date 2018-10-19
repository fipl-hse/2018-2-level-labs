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
     
def propose_candidates(word: str, max_depth_permutations: int = 1):
    candidates_list = []
  
    if word == '' or word is None:
        return []
    if isinstance(max_depth_permutations, int) is False or max_depth_permutations <= 0:
        return []

    candidates_list.append(word[1:])
    for i in range(len(word) - 1):
        candidate = word[:i] + word[i + 1:]
        if candidate not in candidates_list:
            candidates_list.append(candidate)
    if word[:len(word) - 1] not in candidates_list:
        candidates_list.append(word[:len(word) - 1])

    for letter in LETTERS:
        candidate = letter + word
        if candidate not in candidates_list:
            candidates_list.append(candidate)
    for i in range(len(word)):
        for letter in LETTERS:
            candidate = word[:i] + letter + word[i:]
            if candidate not in candidates_list:
                candidates_list.append(candidate)
    for letter in LETTERS:
        candidate = word + letter
        if candidate not in candidates_list:
            candidates_list.append(candidate)

    for symbol in word:
        for letter in LETTERS:
            candidate = word.replace(symbol, letter)
            if candidate not in candidates_list:
                candidates_list.append(candidate)

    for i in range(len(word) - 1):
        candidate = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        if candidate not in candidates_list:
            candidates_list.append(candidate)
    return candidates_list
   
   
def keep_known(candidates: tuple, frequencies: dict):
    known_candidates = []
    if isinstance(candidates, tuple) is False or candidates is None:
        return known_candidates
    else:
        if frequencies is None:
            return known_candidates
        else:
            for word in candidates:
                if word in frequencies:
                    known_candidates.append(word)
    return known_candidates
