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


def propose_candidates(word, max_depth_permutations: int=1):

    if (word != '' and word is not None and max_depth_permutations is not None
            and type(max_depth_permutations) == int):
        if max_depth_permutations <= 0:
            return []
        else:
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
            #permutations = len(changed_to_new) + len(inserted) + len(interchange) + len(deletes)
            all_changes_set = set(all_changes)
            clear_changes = list(all_changes_set)
            return clear_changes

    else:
        return []


pass


def keep_known(candidates: tuple, frequencies: dict) -> list:
    filtered_w = []
    if (type(candidates) == tuple and candidates is not None and candidates != ()
        and frequencies is not None and frequencies != {}):
        for candidate in candidates:
            if candidate in frequencies.keys():
                filtered_w.append(candidate)
        return filtered_w
    else:
        return []


pass


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if frequencies is not None and candidates is not None and frequencies != {}:
        for candidate in candidates:
            if type(candidate) != str:
                list(candidates).remove(candidate)
        new_dict = {}
        for item in frequencies.items():
            if type(item[0]) == str:
                new_dict[item[0]] = item[1]
        if candidates == ():
            return 'UNK'
        else:
            most_frequent = []
            m_freq_key_value = []
            for value in sorted(new_dict.values()):
                if value == max(sorted(new_dict.values())):
                    most_frequent.append(value)
            for item in new_dict.items():
                if item[1] == value:
                    m_freq_key_value.append(item)

            m_freq_key = []
            for item in m_freq_key_value:
                m_freq_key.append(item[0])

            winners = []
            if type(candidates) != tuple:
                candidates = tuple(candidates)
            for candidate in candidates:
                if candidate in m_freq_key:
                    winners.append(candidate)
            sorted_w = sorted(winners)
            chosen_word = sorted_w[0]
            return chosen_word
    else:
        return 'UNK'


pass


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if (frequencies is not None and word is not None
            and frequencies != {} and word != ''):
        if as_is_words is None:
            as_is_words = []
        if word in frequencies or word.upper() in as_is_words:
            return word
        else:
            modifications = propose_candidates(word)
            clean = keep_known(tuple(modifications), frequencies)
            winner = choose_best(frequencies, tuple(clean))
            return winner
    else:
        return 'UNK'

pass


def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
    for old_word in text:
        if old_word.isalpha():
            word = old_word.lower()
            if word in frequencies or word in as_is_words:
                return word
            else:
                modifications = propose_candidates(word)
                clean = keep_known(modifications, frequencies)
                winner = choose_best(frequencies, clean)
                return winner

    

pass
