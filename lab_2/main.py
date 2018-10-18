"""
Labour work #2
 Check spelling of words in the given  text
"""
import sys
sys.path.append("2018-level-labs\lab_1\ ")
import operator
import re
from lab_1.main import calculate_frequences
if __name__ == '__main__':
  with open('very_big_reference_text.txt', 'r') as f:
    REFERENCE_TEXT = f.read()
REFERENCE_TEXT = ''
frequencies = calculate_frequences(REFERENCE_TEXT)
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
as_is_words = ()
max_depth_permutations = 1

def propose_candidates(word: str, max_depth_permutations: int = 1) -> str:
    if max_depth_permutations is None or isinstance(max_depth_permutations, int) != True or max_depth_permutations <= 0:
      return []
    if word is None:
      return []
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
        

def keep_known(candidates: tuple, frequencies: dict) -> list:
    if frequencies is None:
      frequencies = {}
    if candidates is None or isinstance(candidates, tuple) != True:
      candidates = ()
    kn_w = set()
    for i in candidates:
        if i in frequencies:
            kn_w.add(i)
    candidates = kn_w
    return candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:
    word = ''
    best = {}
    out_best = []
    if frequencies is None:
      frequencies = {}
    if candidates is None:
      candidates = ()
    for w, fr in frequencies.items():    
      for wd in candidates:     
          if wd == w:
            best[w] = fr
    if len(best) == 0:
      word = 'UNK'
    else:
      al_eq = max(best.items(), key=operator.itemgetter(1))[0]
      for k, v in best.items():
        if v >= best.get(al_eq):
          out_best.append(k)
      word = sorted(out_best)[0] 
    return word

def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
  if as_is_words is None:
    as_is_words = ()
  if frequencies is None:
      return 'UNK'
  if word is None:
      word = ''
  if word in as_is_words:  
      return word  
  word = choose_best(frequencies, keep_known(propose_candidates(word, max_depth_permutations), frequencies))
  return word

def spell_check_text(frequencies: dict, as_is_words: tuple, TEXT: str):
  w_out = re.findall(r"[\w']+|[.,!?;]", TEXT)
  for word in w_out:
    if word in as_is_words:
        pass
    if word.isalnum() == True:
      w_out[w_out.index(word)] = spell_check_word(frequencies, as_is_words, word)
    else:
      pass
    
  w_out = re.sub(r'\s([?.!"](?:\s|$))', r'\1', ' '.join(w_out))

