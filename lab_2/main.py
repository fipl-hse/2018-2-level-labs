"""
Labour work #2
 Check spelling of words in the given  text
"""
from typing import Set, Any, Union

from lab_1.main import calculate_frequences

import re

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''


def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:
    if type(max_depth_permutations) is int and type(word) is str and max_depth_permutations > 0 and word != "":
        all_variants = []
        fourth_type = []
        third_type = []
        if len(word) > 1:
            first_type = [word[0:i] + word[i + 1:] for i in range(len(word))]
            for i in range(len(word)):
                neighbor_letters = word[i:i + 2]
                permutations = neighbor_letters[::-1]
                fourth_type.append(word[0:i] + permutations + word[i + 2:])
            for letter in LETTERS:
                third_type.extend([word[0:i] + letter + word[i + 1:] for i in range(len(word))])
        else:
            first_type = [""]
            for letter in LETTERS:
                third_type.extend([word + letter, letter + word])
        second_type = []
        for letter in LETTERS:
            if len(word) > 1:
                second_type.extend([word + letter])
                second_type.extend([word[0:i] + letter + word[i:] for i in range(len(word))])
            else:
                second_type.extend([letter])
        all_variants.extend(first_type)
        all_variants.extend(second_type)
        all_variants.extend(third_type)
        all_variants.extend(fourth_type)
        return list(set(all_variants))
    else:
        return []


def keep_known(candidates: tuple, frequencies: dict) -> list:
    # return [candidate for candidate in candidates if candidate in frequencies] if (type(candidates) is tuple) and (
    #       type(frequencies) is dict) else []
    if type(frequencies) is dict and type(candidates) is tuple:
        best_candidates = []
        for candidate in candidates:
            if candidate in frequencies:
                best_candidates.append(candidate)
        return best_candidates
    else:
        return []


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if candidates == () or frequencies == {}:
        return 'UNK'
    if candidates is None or frequencies is None:
        return 'UNK'

    else:
        list= keep_known(candidates, frequencies)
        frequencies1 = {}

        for element in list:
            for key, value  in frequencies.items():
                if key in list:
                    frequencies1[key] = value
        list1 = sorted(frequencies1.items(), key=lambda x:x[1])
        list1.reverse()
        result = list1[0][0]
    return  result


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if type(frequencies) is not dict or  type(word) is not str:
        return 'UNK'
    if  type(as_is_words) is not tuple:
        pass
    else:
        if word.upper() in as_is_words:
            return word

    if word in frequencies:
        return word
    return choose_best(frequencies, tuple(keep_known(tuple(propose_candidates(word)), frequencies)))


if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)
    test_text = '''As his position grew more responsible, his business connections increased. He already knew a number of rich businessmen who dealt with the bank where he worked. The brokers knew him as representing a well-known film and considered him to be a most reliable person.
Young Cowperwood took an interest in his father's progress. He was quite often allowed to come to the bank on Saturdays, when he would watch with great interest the quick exchange of bills. He wanted to know where all the different kinds of money came from, and what the men did with all the money they received. His father, pleased at his interest, was glad to explain, so that even at this early age — from ten to fifteen — the boy gained a wide knowledge of the condition of the country financially. He was also interested in stocks and bonds, and he learned that some stocks and bonds were not even worth the paper they were written on, and others were worth much more than their face value showed.
At home also he listened to considerable talk of bysiness and financiial adventure.Frank realized that his father was too honest, too careful. He often told himself that when he grew up, he was going to be a broker, or a financier, or a banker, and do some of the risky things he so often used to hear about.
Just at this time there came to the Cowperwoods an uncle, Seneca Davis, who had not appeared in the life of the family before.
Henry Cowperwood was pleased at the arival of this rather rich relative, for before that Seneca Davis had not taken much notice of Henry Cowperwood and his family.
This time, however, he showed much more interest in the Cowperwoods, particularly in Frank.
"How would you like to come down to Cuba and be a planter, my boy?" he asked him once.
"I am not so sure that I'd like to," replied the boy.'''
