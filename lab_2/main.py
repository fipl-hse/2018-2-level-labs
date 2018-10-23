"""
Labour work #2
 Check spelling of words in the given  text
"""

#from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

def propose_candidates(word: str, max_depth_permutations: int = 1) -> str:
    if not word or word == '' or not isinstance(max_depth_permutations, int):
        return []
    if max_depth_permutations <= 0:
        return[]
    candidates_list = set()
    for position in range(len(word)):
        candidates = (word[:position] + word[position + 1:])
        candidates_list.add(candidates)
    for position in range(len(word)):
        for symbol in LETTERS:
            candidates = (word[:position] + symbol + word[position:])
            candidates_list.add(candidates)
            if position == 0:
                candidates = symbol + word
                candidates_list.add(candidates)
    for position in range(len(word) + 1):
        for symbol in LETTERS:
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
    for word in candidates:
        if word in frequencies:
            known_candidates.append(word)
    return known_candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:
    if (not isinstance(candidates, tuple)) or (not isinstance(frequencies, dict)):
        return 'UNK'
 #  if candidates is () or len(frequencies) <= 0:
  #      return 'UNK'
    itog_list = 0
    fine_word = ''
    best_candidates_list = []
  #  for true_candidate in candidates:
   #     if true_candidate not in frequencies:
   #         continue
    #    best_candidates_list.append(true_candidate)

#    new_freq_dict = {}
    new_freq_dict = frequencies.copy()
    spisok = list(frequencies.keys())
    for word in spisok:
        if not isinstance(word, str):
            new_freq_dict.pop(word)
 #   new_freq_dict_extra = dict(new_freq_dict)
#    for best_candidate in best_candidates_list:
 #       new_freq_dict[best_candidate] = frequencies[best_candidate]
    for best_candidate in candidates:
  #      if new_freq_dict[best_candidates_list[best_candidate]] < new_freq_dict[best_candidates_list[best_candidate + 1]]:
 #           if best_candidates_list[best_candidate] in new_freq_dict_extra:
  #              new_freq_dict_extra.pop(best_candidates_list[best_candidate])
        if new_freq_dict[best_candidates_list[best_candidate]] > itog_list:
            itog_list = new_freq_dict[best_candidates_list[best_candidate]]
            fine_word = best_candidate
      #      new_freq_dict_extra.pop(best_candidates_list[best_candidate + 1])
        if new_freq_dict[best_candidates_list[best_candidate]] == itog_list and best_candidate:
            itog_list = new_freq_dict[best_candidates_list[best_candidate]]
            fine_word = best_candidate
    return fine_word



  #  itog_list = []
 #   for word in new_freq_dict_extra.keys():
 #       itog_list.append(word)
  #  itog_list.sort()
  #  fine_word = itog_list[0]
 #   return fine_word

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
    itog_word = choose_best(frequencies, tuple(list_known_candidates))
    return itog_word
