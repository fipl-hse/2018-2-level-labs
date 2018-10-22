 '''Labour work1'''
def read_from_file(path_to_file, lines_limit: int) -> str:             
    my_text = ''
    count_lines = 0
    my_file = open(path_to_file, 'r')
    for line in my_file.read():
        if count_lines == lines_limit:
            return my_text
        my_text += line
        count_lines += 1
    my_file.close()
    return my_text


def calculate_frequences(text: str) -> dict:
    first_dict = {}
    list_of_marks = [
                    '.', ',', ':', '"', '`', '[', ']',
                    '?', '!', '@', '&', "'", '-',
                    '$', '^', '*', '(', ')',
                    '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                    ]
    try:
        elements = text.split()
    except AttributeError:
        return first_dict
    for thing in elements:
        if thing.isdigit():
            continue
        for mark in list_of_marks:
            if mark in thing:
                pos_mark = thing.find(mark)
                thing = thing[:pos_mark] + thing[pos_mark + 1:]
            thing = thing.strip(mark)
        thing = thing.lower()
        first_dict[thing] = first_dict.get(thing, 0) + 1
    if '' in first_dict.keys():
        first_dict.pop('')
    return first_dict


def filter_stop_words(first_dict: dict, stop_words: list) -> dict:
    third_dict = {}
    try:
        second_dict = first_dict.copy()
    except AttributeError:
        return {}
    if first_dict is None or stop_words is None:
        return {}
    for stop_word in stop_words:
        if stop_word in second_dict.keys():
            second_dict.pop(stop_word)
    for key in second_dict.keys():
        try:
            if 0 <= key < 0:
                continue
        except TypeError:
            third_dict[key] = first_dict[key]
    return third_dict


def get_top_n(third_dict: dict, top_n: int) -> tuple:
    list_of_value_key = []
    list_of_top_words = []
    count = 0
    if top_n < 0:
        return ()
    for key, value in third_dict.items():
        list_of_value_key.append([value, key])
    list_of_value_key.sort(reverse=True)
    for item in list_of_value_key:
        if count == top_n:
            break
        list_of_top_words.append(item[1])
        count += 1
    return tuple(list_of_top_words)


def write_to_file(path_to_file: str, content: tuple):
    my_file = open(path_to_file, 'w')
    for word in content:
        my_file.write(word + '\n')
    my_file.close()

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

def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if (not word) or (not isinstance(max_depth_permutations, int)):
        return[]
    if max_depth_permutations <= 0:
        return[]
    candidates_list = set()
    for position in range(len(word)):
        candidates = (word[:position] + word[position + 1:])
        candidates_list.add(candidates)
    for position in range(len(word)):
        for symbol in LETTERS:
            candidates = (word[:position] + symbol + word[position:])
            candidates_list.add(candidates)
    for position in range(len(word) + 1):
        for symbol in LETTERS:
            candidates = (word[:position] + symbol + word[position + 1:])
            candidates_list.add(candidates)
    for position in range(len(word) - 1):
        candidates = (word[:position] + word[position + 1] + word[position] + word[position + 2:])
        candidates_list.add(candidates)
    return list(candidates_list)

def keep_known(candidates: tuple, frequencies: dict) -> list:
    if (not isinstance(candidates, tuple)) or (not isinstance(frequencies, dict)):
        return[]
    known_candidates = []
    for word in candidates:
        if word in frequencies:
            known_candidates.append(word)
    return known_candidates

def choose_best(frequencies: dict, candidates: tuple) -> str:
    if (not candidates) or (not frequencies):
        return 'UNK'
    if (candidates is ()) or (frequencies == dict()):
        return 'UNK'

    best_candidates = []
    for candidate in candidates:
        if not isinstance(candidate, str):
            continue
        if candidate not in frequencies:
            continue
        best_candidates.append(candidate)
    if best_candidates is []:
        return 'UNK'

    new_freq_dict = {}
    for best_candidate in best_candidates:
        new_freq_dict[best_candidate] = frequencies[best_candidate]

    for best_candidate in range(0, len(best_candidates) - 1):
        if new_freq_dict[best_candidates[best_candidate]] < new_freq_dict[best_candidates[best_candidate + 1]]:
            if best_candidates[best_candidate] in new_freq_dict:
                new_freq_dict.pop(best_candidates[best_candidate])
        if new_freq_dict[best_candidates[best_candidate]] > new_freq_dict[best_candidates[best_candidate + 1]]:
            new_freq_dict.pop(best_candidates[best_candidate + 1])
        if new_freq_dict[best_candidates[best_candidate]] == new_freq_dict[best_candidates[best_candidate + 1]]:
            continue

    itog_list = []
    for word in new_freq_dict.keys():
        itog_list.append(word)
    itog_list.sort()
    true_word = itog_list[0]
    return true_word
