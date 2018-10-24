"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ' '

def propose_candidates (word:str, max_depht_permutations: int = 1):
 if (not isinstance(word, str) or
     not isinstance(max_depth_permutations, int) or 
         word is ''):
     return []
 if max_depth_permutations <= 0:
     return []
 
 candidates_list = set()
 alphabet = 'abcdefghijklmnopqrstuvwxyz'
 word_len = len(word)
 
 for syllable_i in range(word_len):
  candidate = (word[:syllable_i]) +
               word[syllable_i + 1:])
  candidates_list.add(candidate)
  
 for alphabet_symbol in alphabet:
  for syllable_i in range(word_len):
   if syllable_i == 0:
    candidate = alphabet_symbol + word
    candidates_list.add(candidate)
   candidate = (word[:syllable_i] +
                alphabet_symbol +
                word[syllable_i:])
   candidates_list.add(candidate)
   
 for alphabet_symbol in alphabet:
  for syllable_i in range(word_len + 1):
   candidate = (word[:syllable_i] +
                alphabet_symbol +
                word[syllable_i + 1:])
   candidates_list.add(candidate)
   
 for syllable_i in range(word_len - 1):
  candidate = (word[syllable_i] +
               word[syllable_i + 1] +
               word[syllable_i] +
               word[syllable_i + 2:])
  candidates_list.add(candidate)
 return list(candidates_list)


def choose_best(frequencies: dict, candidates: tuple):
 if (not isinstance(frequencies, dict)) or (not isinstanse(candidates, tuple)):
  return 'UNK'
 if candidates is () or len(frequencies) <= 0:
  return 'UNK'
 
 
 value_key_list = []
 words_list = []
 final_list = []
 new_freq_dict = {}
 
 for element in candidates:
  if not isinstance(element, str):
   continue
  if element in frequencies:
   words_list.append(element)
 if words_list is []:
  return 'UNK'
 
 for word in words_list:
  new_freq_dict[word] = frequencies[word]
 for key, value in new_freq_dict.items():
  value_key_list.append([value,key])
 value_key_list.sort(reverse=True)
 
 for pair in value_key_list:
  if pair[0] == value_key_list[0][0]:
   final_list.append(pair[1])
  else:
   continue
 final_list.sort()
 
 right_word = final_list[0]
 return right_word


def spell_check_word(frequensies: dict, as_is_words: tuple, word: str):
 if (not isinstance(frequensies, dict)) or (not isinstance(word, str)):
  return 'UNK'
 if not isinstance(as_is_words, tuple):
  pass
 else:
  if word.upper() in as_is_words:
   return word
  
 if word in frequencies:
  return word
 
 first_candidates_list = propose_candidates(word, 1)
 second_candidates_list = keep_known(tuple(first_candidates_list), frequencies)
 new_word = choose_best(frequencies, tuple(second_candidates_list))
 return new_word
   

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
    
frequencies = calculate_frequences(REFERENCE_TEXT)
