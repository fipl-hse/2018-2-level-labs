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
    if frequencies is None or frequencies == {}:
        return 'UNK'
    if candidates is None or candidates == []:
        return 'UNK'
    if frequencies is not None:
        max_frequent = []
        sorted_frequencies = sorted(frequencies)
        for match in sorted_frequencies:
            if match[1] == sorted_frequencies[0][1]:
                max_frequent.append(match)
        list_of_max_freq = []
        for match in max_frequent:
            list_of_max_freq.append(match[0])
        if candidates != []:
            for cand in candidates:
                if cand in list_of_max_freq:
                    return cand
        else:
            return 'UNK'

def spell_check_word(frequencies, as_is_words, word):
    if word in frequencies or word in as_is_words:
        return word
    else:
        changes = propose_candidates(word)
        clear = keep_known(changes, frequencies)
        the_best = choose_best(frequencies, clear)
        return the_best
