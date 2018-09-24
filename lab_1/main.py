"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""



def calculate_frequences(texts: str) -> dict:

    my_first_dict = {}
    new_bykva = ''

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
        for bykva in texts:
            count_bykva = 1
            for part in bykva:
                if part not in errors:
                    new_bykva += part
            if new_bykva != '':
                if new_bykva not in my_first_dict
                    my_first_dict[bykva] = count_bykva
                else:
                    new_count_bykva = my_first_dict[new_bykva] + 1
                    my_first_dict[new_bykva] = new_count_bykva
        #    count_bykva = texts_list.count(bykva)

    return my_first_dict

def filter_stop_words(my_first_dict: dict, STOP_WORDS: tuple) -> dict:

    if my_first_dict is None:
        return {}
    if STOP_WORDS is None:
        return {}

    my_second_dict = my_first_dict.copy()

    for new_stop_word in STOP_WORDS:
        if new_stop_word in my_second_dict:
            my_second_dict.pop(new_stop_word)
    for key in my_second_dict.keys():
        if type(key) == str and key not in STOP_WORDS:
            my_second_dict[key] = my_first_dict[key]
    return my_second_dict


def get_top_n(my_second_dict: dict, top_n: int) -> tuple:

    top_my_list = []
    if top_n <= 0:
        return()

    for key, value in my_second_dict.items():
        top_my_list.append([value, key])
        tuple_top_n = tuple(top_my_list[:top_n])
    return tuple(top_my_list)
 #my_second_dict = sorted(my_second_dict.items(), key = lambda bykva: bykva[1], reverse = True)




