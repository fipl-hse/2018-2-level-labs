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
def propose_candidates(word: str, max_depth_permutations: int=1) -> list:
    if type(word) == str and word != '' and max_depth_permutations == 1:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        lst1 = []
        lst4 = []

        # удаление 1-ой буквы
        lst2 = list(word)
        lst3 = lst2.copy()
        for i in range(len(lst2)):
            del (lst3[i])
            word2 = ''.join(lst3)
            lst4.append(word2)
            lst3 = lst2.copy()

        # добавить букву в строку
        lst5 = [i for i in word]
        lst6 = lst5.copy()
        lst7 = []
        for i in alphabet:
            for k in range(len(lst5)):
                lst6.insert(k, i)
                word3 = ''.join(lst6)
                lst7.append(word3)
                lst6 = lst5.copy()

        lst8 = [word + i for i in alphabet]
        lst9 = lst7 + lst8


        # замена 1 буквы
        word1 = word
        for i in word1:
            word1 = word
            for k in alphabet:
                a = word1.replace(i, k)
                lst1.append(a)

        # поменять буквы местами

        lst10 = [i for i in word]
        lst11 = lst10.copy()
        lst12 = []

        for i in range(len(lst10) - 1):
            lst11[i], lst11[i + 1] = lst11[i + 1], lst11[i]
            word4 = ''.join(lst11)
            lst12.append(word4)
            lst11 = lst10.copy()

        totallist = lst4 + lst9 + lst1 + lst12
        nodubl = set(totallist)
        candidates = list(nodubl)
        

    else:
        candidates = []
    return candidates
   
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
