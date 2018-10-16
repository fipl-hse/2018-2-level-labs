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
  pass
 
def keep_known(candidates: tuple, frequencies: dict) -> list:
  pass
 
def choose_best(frequencies: dict, candidates: tuple) -> str:
  pass

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
  pass
 
def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
  pass
