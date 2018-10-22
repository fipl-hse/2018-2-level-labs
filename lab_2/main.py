"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

our_text = str()

if __name__ == '__main__':
    # with open('very_big_reference_text.txt', 'r') as f:
    #     our_text = f.read()


def propose_candidates(word: str, max_depths_permutations: int = 1) -> list:
    if word is None or word == '' or max_depths_permutations == str(max_depths_permutations) \
            or max_depths_permutations is None or int(max_depths_permutations) <= 0:
        return []

    del_list = list()
    for word_ind in range(len(word)):
        new_word = word[:word_ind] + word[(word_ind + 1):]
        del_list.append(new_word)

    add_list = list()
    for word_ind in range(len(word) + 1):
        for letter in letters:
            new_word = word[:word_ind] + letter + word[word_ind:]
            add_list.append(new_word)

    ch_list = list()
    for word_ind in range(0, (len(word))):
        for letter in letters:
            new_word = word[:word_ind] + letter + word[(word_ind + 1):]
            ch_list.append(new_word)

    rep_list = list()
    for word_ind in range(1, len(word)):
        new_word = word[:(word_ind - 1)] + word[word_ind] + word[word_ind - 1] + word[(word_ind + 1):]
        rep_list.append(new_word)

    the_copy = del_list + add_list + ch_list + rep_list
    list_of_versions = list()
    for version in the_copy:
        if version in list_of_versions:
            continue
        list_of_versions.append(version)

    if max_depths_permutations > 1:
        add_candidate = list()
        list_of_versions_add = list()
        while max_depths_permutations:
            max_depths_permutations -= 1
            for version in list_of_versions:
                for word_ind in range(len(version)):
                    new_word = version[:word_ind] + version[(word_ind + 1):]
                    add_candidate.append(new_word)

                for word_ind in range(len(version) + 1):
                    for letter in letters:
                        new_word = version[:word_index] + letter + version[word_index:]
                        add_candidate.append(new_word)

                for word_ind in range(0, (len(version))):
                    for letter in letters:
                        new_word = version[:word_index] + letter + version[(word_index + 1):]
                        add_candidate.append(new_word)

                for word_index in range(1, len(version)):
                    new_word = version[:(word_index - 1)] + version[word_index] + version[word_index - 1] + \
                               version[(word_index + 1):]
                    add_candidate.append(new_word)

                for variant in add_candidate:
                    if variant in list_of_versions_add:
                        continue
                    list_of_versions_add.append(variant)
                add_candidate = list()
        return list_of_versions_add

    return list_of_versions


def keep_known(candidates: tuple, frequencies: dict) -> list:
    if candidates is None or type(candidates) is not tuple or frequencies is None:
        return []

    our_variants = list()
    for variant in candidates:
        if str(variant).isdigit():
            continue
        if variant in frequencies:
            our_variants.append(variant)

    return our_variants


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if candidates is () or candidates is None or frequencies == dict() or frequencies is None:
        return 'UNK'

    new_variants = []
    for variant in candidates:
        if variant not in frequencies:
            continue
        new_variants.append(variant)

    new_dict = {}
    for new_variant in new_variants:
        new_dict[new_variant] = frequencies[new_variant]

    new_dict_add = dict(new_dict)
    for new_variant in range(0, len(new_variants) - 1):
        if new_dict[new_variants[new_variant]] > new_dict[new_variants[new_variant + 1]]:
            new_dict_add.pop(new_variants[new_variant + 1])
        if new_dict[new_variants[new_variant]] < new_dict[new_variants[new_variant + 1]]:
            if new_variants[new_variant] in new_dict_add:
                new_dict_add.pop(new_variants[new_variant])
        if new_dict[new_variants[new_variant]] == new_dict[new_variants[new_variant + 1]]:
            continue

    final_res = list()
    for key in new_dict_add.keys():
        final_res.append(key)
    final_res.sort()

    return final_res[0]


def checked_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
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

    first = propose_candidates(word)
    true_candidates = keep_known(tuple(first), frequencies)  # -as_is_words
    final_candidate = choose_best(frequencies, tuple(true_candidates))
    return final_candidate


def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
    symb = [',', '?', '!', '.']
    clean_text = str()
    for symbol in text:
        if symbol in symb:
            clean_text = clean_text + ' ' + symbol
        else:
            clean_text += symbol
    clean_text = clean_text.split()

    correct_list = list()
    for symbol in clean_text:
        if symbol in symb:
            correct_list.append(symbol)
            continue
        if symbol in frequencies:
            correct_list.append(symbol)
            continue
        if symbol[0].isupper():
            new_symbol = symbol.lower()
        if new_symbol in frequencies:
            correct_list.append(symbol)
            continue
        correct_word = checked_word(frequencies, as_is_words, new_symbol)
        for letter in correct_word:
            new_symbol = letter.upper() + correct_word[1:]
            correct_list.append(new_symbol)
            break
    else:
        correct_word = checked_word(frequencies, as_is_words, symbol)
        correct_list.append(correct_word)

    str_text = str()
    for symbol in correct_list:
        str_text = str_text + symbol + ' '

    our_text_str = ''
    for symbol in range(len(str_text)):
        if str_text[symbol] in symb:
            our_text_str = our_text_str[:-1] + str_text[symbol]
            continue
    our_text_str += str_text[symbol]
    return our_text_str 

