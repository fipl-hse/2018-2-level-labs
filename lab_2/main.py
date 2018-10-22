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
def keep_known(candidates: tuple, frequencies: dict) -> list:
    lst = []
    if type(frequencies)== dict:
        frequencies1 = {}
        for k, v in frequencies.items():
            if type(k) == str:
                frequencies1[k] = v
        if type(candidates) == tuple:
            for i in candidates:
                if i in frequencies1:
                    lst.append(i)
        else:
            lst = []
    else:
        lst = []
    return lst


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if candidates == () or type(candidates) != tuple or frequencies == {} or type(frequencies) != dict:
        finalresult = 'UNK'

    else:
        lst = keep_known(candidates, frequencies)

        frequencies1 = {}
        for i in lst:
            for k, v in frequencies.items():
                if k in lst:
                    frequencies1[k] = v
        lst1 = sorted(frequencies1.items(), key=lambda x: x[1])
        lst1.reverse()
        finalresult = lst1[0][0]

    return finalresult
