"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if type(max_depth_permutations) is int and type(word) is str and max_depth_permutations > 0 and word != "":
        all_variants = []
        replace_one = []
        change_one = []
        if len(word) > 1:
            del_one = [word[0:i] + word[i + 1:] for i in range(len(word))]
            for i in range(len(word)):
                adjacent_letters = word[i:i + 2]
                permutation = adjacent_letters[::-1]
                replace_one.append(word[0:i] + permutation + word[i + 2:])
            for letter in LETTERS:
                change_one.extend([word[0:i] + letter + word[i + 1:] for i in range(len(word))])
        else:
            del_one = [""]
            for letter in LETTERS:
                change_one.extend([word + letter, letter + word])
        add_one = []
        for letter in LETTERS:
            if len(word) > 1:
                add_one.extend([word + letter])
                add_one.extend([word[0:i] + letter + word[i:] for i in range(len(word))])
            else:
                add_one.extend([letter])
        all_variants.extend(del_one)
        all_variants.extend(add_one)
        all_variants.extend(change_one)
        all_variants.extend(replace_one)
        return list(set(all_variants))
    else:
        return []


def keep_known(candidates: tuple, frequencies: dict) -> list:
    if candidates is None and frequencies is None and type(candidates) is not tuple:
        return []
    necessary_candidates_list = []
    for necessary_candidate in candidates:
        if necessary_candidate in frequencies:
            necessary_candidates_list.append(necessary_candidate)
    return necessary_candidates_list


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if type(frequencies) is dict and type(candidates) is tuple:
        result = [key for key, value in
                  sorted(sorted((item for item in frequencies.items() if item[0] in candidates), key=lambda x: x[0]),
                         key=lambda x: x[1], reverse=True)]
        return result[0] if len(result) != 0 else 'UNK'
    return 'UNK'


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if type(frequencies) is dict and type(word) is str:
        if type(as_is_words) is tuple and all((type(item) is str for item in as_is_words)) and word in (word.lower() for
                                                                                                        word in
                                                                                                        as_is_words):
            return word
        if word in frequencies.keys():
            return word
        return choose_best(frequencies, tuple(keep_known(tuple(propose_candidates(word)), frequencies)))
    else:
        return "UNK"




if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)
    test_text = '''All afternoon his tractor pulls a flat wagon 
with bales to the barn, then back to the waiting 
chopped field. It trails a feather of smok. 
Down the block we bend with the season: 
shoes to polish for a big game, 
storm windows to batten or patch. 
And how like a fieldt is the whole sky now 
that the maples have shed their laeves, too. 
It makes us believers—stasioned in groups, 
leaning on rakes, looking into space. We rub blisters 
over billows of leaf smoke. Or stand alone, 
bagging gold for the cold days to come.'''