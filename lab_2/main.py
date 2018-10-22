"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences


REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

alphabet = 'abcdefghijklmnoprstquvwxyz'

def propose_candidates(word: str, max_depth_permutations: int=1) -> list:
    candidate_list = []
    if word is None or word == '' or max_depth_permutations != 1:
        return([])
    for index in range(len(word)):
        candidate_list.append(word[:index] + word[index + 1:]) #удаление одной буквы из слова
    for index in range(len(word) - 1):
        candidate_list.append(word[:index] + word[index + 1] + word[index] + word[index + 2:])
    for symbol in alphabet:
        for index in range(len(word) + 1):
            candidate_list.append(word[:index] + symbol + word[index + 1:])  # замена каждой буквы на букву из алфавита
            candidate_list.append(word[:index] + symbol + word[index:])  # добавление одной буквы в каждое место слова
    candidate_list_without_double_words = list(set(candidate_list))
    return candidate_list_without_double_words
    candidate_list_without_double_words = []


def keep_known(candidates: tuple, frequencies: dict) -> list:
    if candidates is None or isinstance(candidates,tuple) is False or candidates == ():
       return([])

    if frequencies is None or frequencies == {}:
        return([])

    cleaned_candidates = []
    for word in candidates:
        if word in frequencies:
            cleaned_candidates.append(word)
    return (cleaned_candidates)

def choose_best(frequencies: dict, candidates: tuple) -> str:
    if candidates == () or candidates is None:
        return('UNK')
    if frequencies is None or frequencies == {}:
        return('UNK')
    necessary_words = []
  

    freq = list(frequencies.values())
    words = list(frequencies.keys())
    for word in words:
        if  not isinstance(word, str):
            frequencies.pop(word)

    max_freq = max(frequencies.values())
    for word, freq in frequencies.items():
        if freq == max_freq:
            necessary_words.append(word)
    necessary_words.sort()
    right_word = necessary_words[0]
    return (right_word)
