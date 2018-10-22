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

candidate_list = []
alphabet = 'abcdefghijklmnoprstquvwxyz'
word ='cat'

def propose_candidates(word: str, max_depth_permutations: int=1) -> list:
    if word is None or word == '' or max_depth_permutations != 1:
       return([])


    for index in range(1,len(word)):
        candidate_list.append(word[:index] + word[index + 1:])  #удаление одной буквы из слова
        candidate_list.append(word[:index+2]+word[index]+word[index+2:])


    for symbol in alphabet:
        for index in range(0, len(word)):
            candidate_list.append(word[:index] + symbol + word[index + 1:])  # замена каждой буквы на букву из алфавита
            candidate_list.append(word[:index] + symbol + word[index:])  # добавление одной буквы в каждое место слова

    candidate_list_without_double_words = []

    for word in candidate_list:
        if word in candidate_list_without_double_words:
            continue

        else:
             candidate_list_without_double_words.append(word)
    return(candidate_list_without_double_words)
