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
    if word != '' and word is not None and isinstance(max_depth_permutations, int) and max_depth_permutations > 0 and max_depth_permutations is not None:
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
      
def keep_known(candidates, frequencies):
    all_filtered_words = []
    if candidates is not None and type(candidates) == tuple and frequencies is not None:
        for cand in candidates:
            if cand in frequencies:
                all_filtered_words.append(cand)
        return all_filtered_words
    else:
        return all_filtered_words

def choose_best(frequencies, candidates):
 if frequencies is None or frequencies == {} or candidates is None:
        return 'UNK'
   else:
        for cand in candidates:
            if type(cand) != str:
                list(candidates).pop(cand)
        new_dictionary = {}
        for object in frequencies.items():
            if type(object[0]) == str:
                new_dictionary[object[0]] = object[1]
        if candidates == ():
            return 'UNK'
        else:
            max_freq = []
            max_freq_key_value = []
            for value in sorted(new_dictionary.values()):
                if value == max(sorted(new_dictionary.values())):
                    max_freq.append(value)
            for object in new_dictionary.items():
                if object[1] == value:
                    max_freq_key_value.append(object)
            max_freq_key = []
            for object in max_freq_key_value:
                max_freq_key.append(object[0])
            the_best = []
            if type(candidates) != tuple:
                candidates = tuple(candidates)
            for cand in candidates:
                if cand in max_freq_key:
                    the_best.append(cand)
            selected = sorted(the_best)
            the_chosen = selected[0]
            return the_chosen


def spell_check_word(frequencies, as_is_words, word):
        if frequencies is None or frequencies == {} or word is None or word == '':
        return 'UNK'
    else:
        if as_is_words is None:
            as_is_words = []
        if word in frequencies or word.upper() in as_is_words:
            return word
        else:
            changes = propose_candidates(word)
            clear = keep_known(tuple(changes), frequencies)
            the_best = choose_best(frequencies, tuple(clear))
            return the_best
