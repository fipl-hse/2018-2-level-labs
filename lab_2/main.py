"""
Labour work #2
 Check spelling of words in the given  text
"""

from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LETTERS.split()

REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)


def propose_candidates(word: str, max_depths_permutations: int = 1) -> list:
    if word is None or (word == '') or (max_depths_permutations == str(max_depths_permutations)) \
            or (max_depths_permutations is None) or (int(max_depths_permutations) <= 0):
        return []

    deleting_list = []
    for word_index in range(len(word)):
        new_word = word[:word_index] + word[(word_index + 1):]
        deleting_list.append(new_word)

    adding_list = []
    for word_index in range(len(word) + 1):
        for letter in LETTERS:
            new_word = word[:word_index] + letter + word[word_index:]
            adding_list.append(new_word)

    changing_list = []
    for word_index in range(0, (len(word))):
        for letter in LETTERS:
            new_word = word[:word_index] + letter + word[(word_index + 1):]
            changing_list.append(new_word)

    replacing_list = []
    for word_index in range(1, len(word)):
        new_word = word[:(word_index - 1)] + word[word_index] + word[word_index - 1] + word[(word_index + 1):]
        replacing_list.append(new_word)

    all_words = deleting_list + adding_list + changing_list + replacing_list
    set(all_words)

    if max_depths_permutations > 1:
        candidate_adding = []
        all_words_adding = []
        while max_depths_permutations:
            max_depths_permutations -= 1
            for element in all_words:
                for word_index in range(len(element)):
                    new_word = element[:word_index] + element[(word_index + 1):]
                    candidate_adding.append(new_word)

                for word_index in range(len(element) + 1):
                    for letter in LETTERS:
                        new_word = element[:word_index] + letter + element[word_index:]
                        candidate_adding.append(new_word)

                for word_index in range(0, (len(element))):
                    for letter in LETTERS:
                        new_word = element[:word_index] + letter + element[(word_index + 1):]
                        candidate_adding.append(new_word)

                for word_index in range(1, len(element)):
                    new_word = element[:(word_index - 1)] + element[word_index] + element[word_index - 1] + \
                               element[(word_index + 1):]
                    candidate_adding.append(new_word)

                for variant in candidate_adding:
                    if variant in all_words_adding:
                        continue
                    else:
                        all_words_adding.append(variant)
                candidate_adding = []
        return all_words_adding
    return all_words


def keep_known(candidates: tuple, frequencies: dict) -> list:
    if candidates is None or (type(candidates) is not tuple) or (frequencies is None):
        return []

    true_candidates = []
    for variant in candidates:
        if str(variant).isdigit():
            continue
        if variant in frequencies:
            true_candidates.append(variant)
    return true_candidates


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if candidates is () or (candidates is None) or (frequencies == dict()) or (frequencies is None):
        return 'UNK'

    new_candidates = []
    for variant in candidates:
        if variant not in frequencies:
            continue
        else:
            new_candidates.append(variant)

    new_dict = {}
    for c in new_candidates:
        new_dict[c] = frequencies[c]
    new_dict_add = dict(new_dict)
    for c in range(0, len(new_candidates) - 1):
        if new_dict[new_candidates[c]] > new_dict[new_candidates[c + 1]]:
            new_dict_add.pop(new_candidates[c + 1])
        if new_dict[new_candidates[c]] < new_dict[new_candidates[c + 1]]:
            if new_candidates[c] in new_dict_add:
                new_dict_add.pop(new_candidates[c])
        if new_dict[new_candidates[c]] == new_dict[new_candidates[c + 1]]:
            continue
    final_result = []
    for key in new_dict_add.keys():
        final_result.append(key)
    final_result.sort()

    return final_result[0]


def checked_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word is None or frequencies is None:
        return 'UNK'
    if as_is_words is None:
        pass
    else:
        if word.upper() in as_is_words:
            return word
    if word in frequencies:
        return word
    first = propose_candidates(word)
    true_candidates = keep_known(tuple(first), frequencies)
    final_candidate = choose_best(frequencies, tuple(true_candidates))
    return final_candidate


def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
    symbols = ['.', ',', '!', '?']
    new_text = ''
    for symbol in text:
        if symbol in symbols:
            new_text = new_text + ' ' + symbol
        else:
            new_text += symbol
    new_text = new_text.split()

    correct_list = []
    for symbol in new_text:
        if symbol in symbols:
            correct_list.append(symbol)
            continue
        if symbol in frequencies:
            correct_list.append(symbol)
            continue
        if symbol[0].isupper():
            symbol_lower = symbol.lower()
        if symbol_lower in frequencies:
            correct_list.append(symbol)
            continue
        correct_word = checked_word(frequencies, as_is_words, symbol_lower)
        for letter in correct_word:
            symbol_lower = letter.upper() + correct_word[1:]
            correct_list.append(symbol_lower)
            break
    else:
        correct_word = checked_word(frequencies, as_is_words, symbol)
        correct_list.append(correct_word)

    str_text = ''
    for symbol in correct_list:
        str_text = str_text + symbol + ' '

    final_text_str = ''
    for symbol in range(len(str_text)):
        if str_text[symbol] in symbols:
            final_text_str = final_text_str[:-1] + str_text[symbol]
            continue
    final_text_str += str_text[symbol]
    return final_text_str

     
