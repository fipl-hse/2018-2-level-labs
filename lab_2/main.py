"""
Labour work #2
 Check spelling of words in the given  text
"""

from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''


# ШАГ 1 из Задания
def propose_candidates(word: str, max_depth_permutations: int = 1):
    if isinstance(word, str) or isinstance(max_depth_permutations, int) or word == '':
        return []
    elif max_depth_permutations <= 0 or max_depth_permutations != 1:
        return []

    alf = 'abcdefghijklmnopqrstuvwxyz'
    length = len(word)
    list_of_words = set()

    # step 1.1: удаление одной буквы
    for i in range(length):
        if i == 0:
            word_mod = word[1:length]
        elif i == length - 1:
            word_mod = word[0:length - 1]
        else:
            word_mod = word[0:i] + word[i + 1:length]
        list_of_words.add(word_mod)

    # step 1.2: добавление буквы
    for element in alf:
        for i in range(length + 1):
            if i == 0:
                word_mod = element + word
            elif i == length:
                word_mod = word + element
            else:
                word_mod = word[0:i] + element + word[i:length]
            list_of_words.add(word_mod)

    # step 1.3: замена буквы
    for element in alf:
        for i in range(length):
            if i == 0:
                word_mod = element + word[1:]
            elif i == length - 1:
                word_mod = word[0:length - 1] + element
            else:
                word_mod = word[0:i] + element + word[i + 1:length]
            list_of_words.add(word_mod)

    # step 1.4: перестановка 2 соседних букв местами
    for i in range(length - 1):
        if i == 0:
            word_mod = word[1] + word[0] + word[2:length]
        elif i == length - 2:
            word_mod = word[0: length - 2] + word[length - 1] + word[length - 2]
        else:
            word_mod = word[0:i] + word[i + 1] + word[i] + word[i + 2:length]
        list_of_words.add(word_mod)
    list_of_words = list(list_of_words)
    return list_of_words

# ШАГ 2 из Задания
def keep_known(candidates: tuple, frequencies: dict) -> list:

    if isinstance(candidates, tuple) == False or isinstance(frequencies, dict) == False:
        return []

    corr_candidates = []

    for word in candidates:
        if word in frequencies:
            corr_candidates.append(word)
    return corr_candidates

# ШАГ 3 из Задания
def choose_best(frequencies: dict, candidates: tuple) -> str:

    if isinstance(candidates, tuple) == False or isinstance(frequencies, dict) == False:
        return 'UNK'

    if not candidates or not frequencies:
        return 'UNK'

    new_dict = {}
    new_list_values = []
    top_cand = []

    for e in candidates:
        if e in frequencies:
            new_dict[e] = frequencies[e]
            new_list_values.append(frequencies[e])

    max_freq = max(new_list_values)

    for e in new_dict:
        if frequencies[e] == max_freq:
            top_cand.append(e)
            top_cand.sort()
            best_cand = top_cand[0]

    return best_cand

# ШАГ 4 из Задания
def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if isinstance(frequencies, dict) == False or isinstance(word, str) == False:
        return 'UNK'
    if isinstance(as_is_words, tuple) == False:
        pass
    else:
        if word.upper() in as_is_words:
            return word

    if word in frequencies:
        return word

    candidates = propose_candidates(word, 1)
    corr_candidates = keep_known(tuple(candidates), frequencies)
    best_cand = choose_best(frequencies, tuple(corr_candidates))

    return best_cand

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()

freq_dict = calculate_frequences(REFERENCE_TEXT)
