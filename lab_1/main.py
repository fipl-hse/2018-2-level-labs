"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""



def calculate_frequences(texts: str) -> dict:

    my_first_dict = {}


    #   texts_list = []
    if not texts:
        return {}
    if texts.isdigit():
        continue
    if isinstance(texts, str):
        texts = texts.lower()
        texts = texts.split(' ')
        texts.replace('\n', ' ')
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
                if new_slovo not in my_first_dict:
                    my_first_dict[new_slovo] = count_bykva
                else:
                    new_count_bykva = my_first_dict[new_slovo] + 1
                    my_first_dict[new_slovo] = new_count_bykva
        #    count_bykva = texts_list.count(bykva)

    return my_first_dict

def filter_stop_words(my_first_dict: dict, STOP_WORDS: tuple) -> dict:

    my_second_dict = my_first_dict.copy()

    if not my_first_dict:
        return my_first_dict
    if not STOP_WORDS :
        return my_first_dict

    for new_stop_word in my_first_dict.keys():
        if not isinstance(new_stop_word, str):
            my_second_dict.pop(new_stop_word)
    for slovo_stop in STOP_WORDS:
        if slovo_stop in my_second_dict:
            my_second_dict.pop(slovo_stop)
    return my_second_dict


def get_top_n(my_second_dict: dict, top_n: int) -> tuple:

    top_my_list = []
    if top_n <= 0:
        return()
    else:
        for slovo_stop in my_first_dict.keys():
            top_my_list.append(slovo_stop)
    tuple_top_n = tuple(top_my_list[:top_n])
    return (tuple_top_n)
#my_second_dict = sorted(my_second_dict.items(), key=lambda new_bykva: new_bykva[1], reverse=True)
#for key, value in my_second_dict.items():
   
