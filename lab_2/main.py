"""
Labour work #2
 Check spelling of words in the given  text
"""
import operator
import re
from lab_1.main import calculate_frequences
if __name__ == '__main__':
  with open('very_big_reference_text.txt', 'r') as f:
    REFERENCE_TEXT = f.read()
frequencies = calculate_frequences(REFERENCE_TEXT)
TEXT = '''Extemity directiion existence ase dashwoods do upt. Securing marianne led welcomed offended but offering six raptures.
Conveying concluded newspaper rapturous oh at. Two indeed suffer saw beyond far former mrs remain.
Occasionnal continuing possession we insensible an sentiments as is.
Law but reasonaby motionless principles she. Has six worse downs far blush rooms above stood. 
'''
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

w_from_text = TEXT.split()
max_depth_permutations = 1
def propose_candidates(word: str, max_depth_permutations: int = 1) -> str:
    candidates = set()
    for i in LETTERS:
        for ch in range(len(word) + 1):
            candidates.add(word[:ch] + i + word[ch:])
    for ch in range(len(word) - 1):
        var = []
        for i in word:
            var.append(i)
        var.insert(ch, var[ch + 1])
        var.pop(ch + 2)
        candidates.add(''.join(var))
    for i in LETTERS:
        for ch in word:
             candidates.add(word.replace(ch, i, 1))
    for ch in word:
        candidates.add(word.replace(ch,'',1))
    return candidates
        
as_is_words = ('famiies')           

def keep_known(candidates: tuple, as_is_words: tuple) -> list:
    kn_w = set()
    for i in candidates:
        if i in as_is_words:
            kn_w.add(i)
        if i in frequencies:
            kn_w.add(i)
    candidates = kn_w
    return candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:
    word = ''
    best = {}
    for wd in candidates:
      for w, fr in frequencies.items():
        if wd == w:
          best[w] = fr
    if len(best) == 0:
      word = 'UNK'
    else:
      word = max(best.items(), key=operator.itemgetter(1))[0]
    return word

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
  
  word = choose_best(frequencies, keep_known(propose_candidates(word, max_depth_permutations), as_is_words))
  return word

def spell_check_text(frequencies: dict, as_is_words: tuple, TEXT: str):
  w_out = re.findall(r"[\w']+|[.,!?;]", TEXT)
  for word in w_out:
    if word.isalnum() == True:
      w_out[w_out.index(word)] = spell_check_word(frequencies, as_is_words, word)
    else:
      pass     
  w_out = re.sub(r'\s([?.!"](?:\s|$))', r'\1', ' '.join(w_out))
  print(w_out)

spell_check_text(frequencies, as_is_words, TEXT)