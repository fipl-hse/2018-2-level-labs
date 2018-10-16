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
 
 if word != '' and word != None:
     l_word = word.lower()
     splits = []
     for i in range(len(l_word)+1):
         splits.append([l_word[:i], l_word[i:]])

     deletes = []
     for left, right in splits:
         if right != '':
             deletes.append(left + right[1:])

     interchange = []
     for i in range(len(l_word)-1):
         interchange.append(l_word[:i] + l_word[i + 1] + l_word[i] + l_word[i + 2:])

     inserted = []
     for letter in LETTERS:
         for i in range(len(l_word) + 1):
             inserted.append(l_word[:i] + letter + l_word[i:])

     changed_to_new = []
     for letter in LETTERS:
         for i in range(len(l_word)):
             changed_to_new.append(l_word[:i] + letter + l_word[i+1:])

     all_changes = changed_to_new + inserted + interchange + deletes
     permutations = len(changed_to_new) + len(inserted) + len(interchange) + len(deletes)
     all_changes_set = set(all_changes)
     clear_changes = list(all_changes_set)

 else:
     clear_changes = []

    
