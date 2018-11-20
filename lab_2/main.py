"""
Labour work #2
 Check spelling of words in the given  text
"""

from lab_1.main import calculate_frequences

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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


def propose_candidates(word: str, max_depths_permutations: int = 1) -> list:
    # Step 0. Test processing.
    if word is None or word == '' or max_depths_permutations == str(max_depths_permutations) \
            or max_depths_permutations is None or int(max_depths_permutations) <= 0:
        return []

    # Step 1. Deleting letter in a given word.
    candidates_list_1 = []
    for word_index in range(len(word)):
        new_word = word[:word_index] + word[(word_index+1):]
        candidates_list_1.append(new_word)

    # Step 2. Adding letter to a given word.
    candidates_list_2 = []
    alphabet_checker = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for word_index in range(len(word)+1):
        for element_letter in alphabet_checker:
            new_word = word[:word_index] + element_letter + word[word_index:]
            candidates_list_2.append(new_word)

    # Step 3. Changing of an every letter in given word.
    candidates_list_3 = []
    for word_index in range(0, (len(word))):
        for element_letter in alphabet_checker:
            new_word = word[:word_index] + element_letter + word[(word_index+1):]
            candidates_list_3.append(new_word)

    # Step 4. Replacing adjacent letters in a given word.
    candidates_list_4 = []
    for word_index in range(1, len(word)):
        new_word = word[:(word_index-1)] + word[word_index] + word[word_index-1] + word[(word_index+1):]
        candidates_list_4.append(new_word)

    # Step 5. Deleting duplicates in candidates_duplicates
    candidates_duplicates = candidates_list_1 + candidates_list_2 + candidates_list_3 + candidates_list_4
    candidates_result = []
    for potential_duplicate in candidates_duplicates:
        if potential_duplicate in candidates_result:
            continue
        candidates_result.append(potential_duplicate)

    # Step 6. Checking for more than one misspell in a word.
    if max_depths_permutations > 1:
        candidates_list_plus = []
        candidates_result_plus = []
        while max_depths_permutations:
            max_depths_permutations -= 1
            for generated_candidate in candidates_result:
                # Step 6.1. Deleting letter in a given word.
                for word_index in range(len(generated_candidate)):
                    new_word = generated_candidate[:word_index] + generated_candidate[(word_index + 1):]
                    candidates_list_plus.append(new_word)

                # Step 6.2. Adding letter to a given word.
                for word_index in range(len(generated_candidate) + 1):
                    for element_letter in alphabet_checker:
                        new_word = generated_candidate[:word_index] + element_letter + generated_candidate[word_index:]
                        candidates_list_plus.append(new_word)

                # Step 6.3. Changing of an every letter in given word.
                for word_index in range(0, (len(generated_candidate))):
                    for element_letter in alphabet_checker:
                        new_word = generated_candidate[:word_index] + element_letter + \
                                   generated_candidate[(word_index + 1):]
                        candidates_list_plus.append(new_word)

                # Step 6.4. Replacing adjacent letters in a given word.
                for word_index in range(1, len(generated_candidate)):
                    new_word = generated_candidate[:(word_index - 1)] + generated_candidate[word_index] \
                               + generated_candidate[word_index - 1] + generated_candidate[(word_index + 1):]
                    candidates_list_plus.append(new_word)

                # Step 6.5. Deleting duplicates in candidates_duplicates_plus
                for potential_duplicate in candidates_list_plus:
                    if potential_duplicate in candidates_result_plus:
                        continue
                    candidates_result_plus.append(potential_duplicate)
                candidates_list_plus = []
        return candidates_result_plus

    return candidates_result


def keep_known(candidates: tuple, frequencies: dict) -> list:
    # as_is_word = tuple
    # if as_is_words is None:
        # return []
    if candidates is None:
        return []
    if type(candidates) is not tuple:
        return []
    if frequencies is None:
        return []

    # Step 1. Compliance check for candidates.
    list_of_true_candidates = []
    for potential_true_candidate in candidates:
        if str(potential_true_candidate).isdigit():
            continue
        # if potential_true_candidate.upper() in as_is_words:
            # list_of_true_candidates.append(potential_true_candidate)
        if potential_true_candidate in frequencies:
            list_of_true_candidates.append(potential_true_candidate)

    return list_of_true_candidates


def choose_best(frequencies: dict, candidates: tuple) -> str:
    # Step 0. Test processing.
    if candidates is () or candidates is None:
        return 'UNK'
    if frequencies == dict() or frequencies is None:
        return 'UNK'

    # Step 1. Finding true candidate.
    new_candidates = []
    for potential_candidate in candidates:
        if potential_candidate not in frequencies:
            continue
        new_candidates.append(potential_candidate)

    # Step 0.1 Coping with noisy second test.
    new_dict = {}
    for new_candidate in new_candidates:
        new_dict[new_candidate] = frequencies[new_candidate]
    new_dict_plus = dict(new_dict)
    for new_candidate in range(0, len(new_candidates)-1):
        if new_dict[new_candidates[new_candidate]] > new_dict[new_candidates[new_candidate+1]]:
            new_dict_plus.pop(new_candidates[new_candidate+1])
        if new_dict[new_candidates[new_candidate]] < new_dict[new_candidates[new_candidate+1]]:
            if new_candidates[new_candidate] in new_dict_plus:  # this is because of incorrect copy(checked in class)
                new_dict_plus.pop(new_candidates[new_candidate])
        if new_dict[new_candidates[new_candidate]] == new_dict[new_candidates[new_candidate+1]]:
            continue

    final_ones = []
    for key in new_dict_plus.keys():
        final_ones.append(key)
    final_ones.sort()
    # Step 2. Using function from lab1 to get the most popular candidate.
    # final_candidate = get_top_n(new_dict, 1)

    return final_ones[0]  # final_candidate[0]


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word is None:
        return 'UNK'
    if as_is_words is None:
        pass
    else:
        if word.upper() in as_is_words:
            return word
    if frequencies is None:
        return 'UNK'
    if word in frequencies:
        return word
    first_ones = propose_candidates(word)
    true_candidates = keep_known(tuple(first_ones), frequencies)  # -as_is_words
    final_candidate = choose_best(frequencies, tuple(true_candidates))
    return final_candidate


def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
    symbols_to_save = ['.', ',', '!', '?']

    # Step 1. Making our text possible to split with punctuation symbols.
    new_text = ''
    for element in text:
        if element in symbols_to_save:
            new_text = new_text + ' ' + element
        else:
            new_text += element
    new_text = new_text.split()

    # Step 2. Making a list of words with correct ones and saved punctuation symbols.
    new_list_correct = []
    for element in new_text:
        if element in symbols_to_save:
            new_list_correct.append(element)
            continue
        if element in frequencies:
            new_list_correct.append(element)
            continue
        if element[0].isupper():  # checking if word given has capital letter and saving this letter.
            new_element = element.lower()
            if new_element in frequencies:
                new_list_correct.append(element)
                continue
            correct_word = spell_check_word(frequencies, as_is_words, new_element)
            for letter in correct_word:
                new_element = letter.upper() + correct_word[1:]
                new_list_correct.append(new_element)
                break
        else:
            correct_word = spell_check_word(frequencies, as_is_words, element)
            new_list_correct.append(correct_word)

    # Step 3. Making new string out of correct list.
    new_str_text = ''
    for element in new_list_correct:
        new_str_text = new_str_text + element + ' '

    # Step 4. Making identical text with corrected words.
    new_str_text_final = ''
    for element_letter in range(len(new_str_text)):
        if new_str_text[element_letter] in symbols_to_save:
            new_str_text_final = new_str_text_final[:-1] + new_str_text[element_letter]
            continue
        new_str_text_final += new_str_text[element_letter]

    return new_str_text_final


# The first word will be 'has', not 'this',
# because program deletes symbols (first one) and finds 'has' in dictionary,
# and obviously 'has' is more frequent than 'this'.
# Other mistakes have been found correctly.
string = 'Thas is My Tezt, to Chekc Punctyation. Tahank yuo for watching? Bapital Leters included...'
big_dict = calculate_frequences(REFERENCE_TEXT)
str_final = spell_check_text(big_dict, (), string)
# print(str_final)
