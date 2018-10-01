"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1 import main

REFERENCE_TEXT = ''


def propose_candidates(word: str, max_depth_permutations: int = 1) -> str:
    pass


def keep_known(candidates: tuple, as_is_words: tuple) -> list:
    pass


def choose_best(frequencies: dict, candidates: tuple) -> str:
    pass


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    pass


if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
