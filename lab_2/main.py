"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''
AS_IS_WORDS = ('a', 'an', 'the')

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

TEXT_WITH_MISTAKES = 'She has a dag.'

def one_letter_to_another(word):
    list = []
    for index in enumerate(word):
        index_word = index[0]
        for symbol in LETTERS:
            list.append(word[:index_word] + symbol + word[index_word + 1:])
    return list


def add_one_letter(word):
    list = []
    for index in range(len(word) + 1):
        for symbol in LETTERS:
            list.append(word[:index] + symbol + word[index:])
    return list


def delete_one_letter(word):
    list = []
    for index in enumerate(word):
        index_word = index[0]
        list.append(word[:index_word] + word[index_word + 1:])
    return list


def transposition_two_letters(word):
    list = []
    for index in range(len(word) - 1):
        list.append(word[:index] + word[index + 1] + word[index] + word[index + 2:])
    return list


def propose_candidates(word: str, max_depth_permutations: int=1) -> list:
    final_list = []
    if word and isinstance(max_depth_permutations, int) and max_depth_permutations >= 1:
        list_1 = one_letter_to_another(word)
        list_2 = add_one_letter(word)
        list_3 = delete_one_letter(word)
        list_4 = transposition_two_letters(word)
        not_sorted_list = list_1 + list_2 + list_3 + list_4
        final_list = list(set(not_sorted_list))
    return final_list


def keep_known(candidates, frequent_dict) -> list:
    known_candidates = []
    if isinstance(candidates, tuple):
        if candidates and frequent_dict:
            for word in frequent_dict.keys():
                if word in candidates:
                    known_candidates.append(word)
    return(known_candidates)


def choose_best(frequent_dict, candidates) -> str:
    current_frequent_dict = {}
    finalists = []
    if candidates and frequent_dict:
        for word in candidates:
            if word in frequent_dict.keys():
                current_frequent_dict[word] = frequent_dict[word]
            else:
                current_frequent_dict[word] = 0
    if current_frequent_dict:
        max_frequency = max(current_frequent_dict.values())
        for word, frequency in current_frequent_dict.items():
            if frequency == max_frequency:
                finalists.append(word)
    if len(finalists) == 1:
        return(finalists[0])
    elif len(finalists) >= 2:
        return(min(finalists))
    else:
        return('UNK')

     
def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    most_frequent_candidate = 'UNK'
    if word:
        if as_is_words:
            if (word.upper() in as_is_words) or (word.lower() in as_is_words):
                most_frequent_candidate = word
            else:
                if frequencies:
                    if word not in frequencies.keys():
                        candidates = propose_candidates(word)
                        known_candidates = keep_known(tuple(candidates), frequencies)
                        most_frequent_candidate = choose_best(frequencies, tuple(known_candidates))
        else:
            if frequencies:
                if word not in frequencies.keys():
                    candidates = propose_candidates(word)
                    known_candidates = keep_known(tuple(candidates), frequencies)
                    most_frequent_candidate = choose_best(frequencies, tuple(known_candidates))
    return most_frequent_candidate


# def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
#     prepared_text = (text.split('.'))
#     text_without_mistakes = ''
#     for sentence in prepared_text:
#         text_without_mistakes_list = []
#         sentence_without_mistakes = ''
#         sentence_to_set_of_words = sentence.split(' ')
#         for word in sentence_to_set_of_words:
#             if word not in frequencies.keys():
#                 most_possible_word = spell_check_word(frequencies, as_is_words, word.lower())
#                 text_without_mistakes_list.append(most_possible_word)
#             else:
#                 text_without_mistakes_list.append(word)
#         sentence_without_mistakes += ' '.join(text_without_mistakes_list)
#         sentence_without_mistakes += '.'
#         text_without_mistakes = sentence_without_mistakes.capitalize() + ' '
#     return text_without_mistakes
