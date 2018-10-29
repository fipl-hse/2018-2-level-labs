"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences
import string
import operator

def propose_candidates(word: str, max_depth_permitations: int=1) -> list:
        candidates = list()
        alpha = list(string.ascii_lowercase)
        for i in range(0, len(word) + 1):
            if i < len(word):
                if i < len(word) - 1:
                    c = list(word)
                    c[i], c[i+1] = c[i+1], c[i]
                    candidates.append(''.join(c))
                candidates.append(word[:i] + word[i+1:])
                for c in alpha:
                    candidates.append(word[:i] + c + word[i+1:])                    
            for c in alpha:
                candidates.append(word[:i] + c + word[i:])
        candidates = sorted(list(set(candidates)))
        return candidates

def keep_known(candidates: tuple, frequencies: dict) -> list:
    result = list()
    for word in candidates:
        if word in frequencies.keys():
            result.append(word)
    return result		

def choose_best(frequencies: dict, candidates: tuple) -> str:
    freq_sort = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)
    if len(freq_sort) == 0:
        return 'UNK'
    results = list()
    i = 0;
    for o in freq_sort:
        if o[0] in candidates:
            break
        i += 1
    max_value = freq_sort[i][1]
    for o in freq_sort:
        if o[1] == max_value and o[0] in candidates:
            results.append(o[0])
    return sorted(results)[0]
	
def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word in frequencies or word in as_is_words:
        return word
    candidates = propose_candidates(word)
    candidates = keep_known(candidates, frequencies)
    return choose_best(frequencies, candidates)
	
def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:
    result = ""
    for word in text.split(' '):
        capital_letter = False
        word_ending = " "
        if not word[0] in string.ascii_lowercase:
            capital_letter = True
        if not word[len(word)-1] in string.ascii_lowercase:
            word_ending = word[len(word) - 1] + word_ending
        word = spell_check_word(frequencies, as_is_words, word)
        if capital_letter:
            word.capitalize()
        word += word_ending
        result += word
        
	
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

test_list = propose_candidates("apple")
print(test_list)

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)

