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
     
def propose_candidates(word, max_depth_permutations: int = 1):
    if word != '' and word is not None and max_depth_permutations > 0 and type(max_depth_permutations) == int:
            low_word = word.lower()
            split_list = []
            for i in range(len(low_word) + 1):
                split_list.append([low_word[:i], low_word[i:]])
            delete_list = []
            for left_part, right_part in split_list:
                if right_part != '':
                    delete_list.append(left_part + right_part[1:])
            inside_change = []
            for i in range(len(low_word) - 1):
                inside_change.append(low_word[:i] + low_word[i + 1] + low_word[i] + low_word[i + 2:])
            pasted = []
            for symbol in LETTERS:
                for i in range(len(low_word) + 1):
                    pasted.append(low_word[:i] + symbol + low_word[i:])
            changed = []
            for symbol in LETTERS:
                for i in range(len(low_word)):
                    changed.append(low_word[:i] + symbol + low_word[i + 1:])
            fully_changed = changed + pasted + inside_change + delete_list
            fully_changed_kit = set(fully_changed)
            result_changes = list(fully_changed_kit)
            return result_changes
    else:
        result_changes = []
        return result_changes
      
def keep_known(candidates, as_is_words, frequencies):
    all_filtered_words = []
    iа frequencies != None and candidates != None and type(candidates) != tuple:
        for cand_key in frequencies.keys():
            if cand_key in candidates:
                all_filtered_words.append(cand_key)
        return all_filtered_words
    else:
        return all_filtered_words
