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
        return []
    if frequencies is None:
        return []
    for word in candidates:
        if word in frequencies:
            known_candidates.append(word)
    return known_candidates

   
def choose_best(frequencies: dict, candidates: tuple):
    best_candidate = ''
    if candidates == () or candidates is None:
        return 'UNK'
    if frequencies == {} or frequencies is None:
        return 'UNK'
    candidates_to_sort = []
    for i in range(len(candidates)):
        if candidates[i] in frequencies:
            candidates_to_sort.append(candidates[i])
    if len(candidates_to_sort) == 1:
        best_candidate = candidates_to_sort[0]
    else:
        for i in range(len(candidates_to_sort) - 1):
            if frequencies[candidates_to_sort[i]] > frequencies[candidates_to_sort[i + 1]]:
                best_candidate = candidates[i]
            elif frequencies[candidates_to_sort[i]] == frequencies[candidates_to_sort[i + 1]]:
                alphabet_sorting = [candidates_to_sort[i], candidates_to_sort[i + 1]]
                alphabet_sorting.sort()
                best_candidate = alphabet_sorting[0]
            else:
                best_candidate = candidates_to_sort[i + 1]
    return best_candidate  
   

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str):
    if frequencies is None or word is None:
        return 'UNK'
    elif word in frequencies or as_is_words is not None and word.upper() in as_is_words:
        return word
    else:
        candidates = propose_candidates(word, max_depth_permutations=1)
        candidates = tuple(candidates)
        known_candidates = keep_known(candidates, frequencies)
        known_candidates = tuple(known_candidates)
        best_candidate = choose_best(frequencies, known_candidates)
        return best_candidate   
