"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""



def calculate_frequences(texts: str) -> dict:

    freq_dictionary = {}


    #   texts_list = []
    if not texts:
        return {}
    if isinstance(texts, str):
        texts = texts.lower()
        texts = texts.split(' ')
        texts.remove('\n', ' ')
        while '\n' in texts:
            texts.remove('\n')
        while texts.find(' ') != -1:
            texts = texts.replace(' ', '')

        errors = ['0','1','2','3','4','5','6','7','8','9',
                  '!','?','.',',','_','-','@','#','$','&',
                  '^','%','*','=','-','+','/',']','[',
                  '>','<',':',';','{','}','~','"','`','"'
                  ]
        print(texts)
        for slovo in texts:
            new_slovo = ''
            count_bykva = 1
            for part in slovo:
                if part not in errors:
                    new_slovo += part
            if new_slovo != '':
                if new_slovo not in freq_dictionary:
                    freq_dictionary[new_slovo] = count_bykva
                else:
                    new_count_bykva = freq_dictionary[new_slovo] + 1
                    freq_dictionary[new_slovo] = new_count_bykva
        #    count_bykva = texts_list.count(bykva)

    return  freq_dictionary

def filter_stop_words(freq_dictionary: dict, STOP_WORDS: tuple) -> dict:

    freq_dictionary_new = freq_dictionary.copy()

    if not  freq_dictionary:
        return  freq_dictionary
    if not STOP_WORDS :
        return  freq_dictionary

    for new_stop_word in freq_dictionary.keys():
        if not isinstance(new_stop_word, str):
            freq_dictionary_new.pop(new_stop_word)
    for slovo_stop in STOP_WORDS:
        if slovo_stop in freq_dictionary_new:
            freq_dictionary_new.pop(slovo_stop)
    return freq_dictionary_new


def get_top_n(freq_dictionary_new: dict, top_n: int) -> tuple:

    top_my_list = []
    if top_n <= 0:
        return()
    else:
        for slovo_stop in freq_dictionary.keys():
            top_my_list.append(slovo_stop)
    tuple_top_n = tuple(top_my_list[:top_n])
    return (tuple_top_n)
#my_second_dict = sorted(my_second_dict.items(), key=lambda new_bykva: new_bykva[1], reverse=True)
#for key, value in my_second_dict.items():



