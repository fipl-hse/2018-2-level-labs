
Labour work #2
 Check spelling of words in the given  text
"""

from lab_1.main import calculate_frequences
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ' '

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)
        FREQ_DICT = calculate_frequences(REFERENCE_TEXT)


def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if (not word) or (not isinstance(max_depth_permutations, int)):
        return[]
    if max_depth_permutations <= 0:
        return[]

#candidates_list = []
candidates_list = set()
    for position in range(len(word)):
#        position_word = position[0]
        candidates = (word[:position] + word[position + 1:])
        candidates_list.add(candidates)

 #  for position in range(len(word) + 1):
    for position in range(len(word)):
        for symbol in LETTERS:
            candidates = (word[:position] + symbol + word[position:])
            candidates_list.add(candidates)

 #  for position in enumerate(word):
    for position in range(len(word) + 1):
  #     position_word = position[0]
        for symbol in LETTERS:
            candidates = (word[:position] + symbol + word[position + 1:])
            candidates_list.add(candidates)

    for position in range(len(word) - 1):
        candidates = (word[:position] + word[position + 1] + word[position] + word[position + 2:])
        candidates_list.add(candidates)

    return list(candidates_list)
