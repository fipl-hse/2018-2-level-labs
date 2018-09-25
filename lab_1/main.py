"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""



def calculate_frequences(text: str) -> dict:
    freq_dict = {}
    #   texts_list = []
    if not text:
        return {}
    if isinstance(text, str):
        text = text.lower()
        text.replace('\n', ' ')
        text_list = text.split(' ')
        while text.find(' ') != -1:
            text = text.replace(' ', '')
        while '\n' in text_list:
            text_list.remove('\n')
        errors = ['0','1','2','3','4','5','6','7','8','9',
                  '!','?','.',',','_','-','@','#','$','&',
                  '^','%','*','=','-','+','/',']','[',
                  '>','<',':',';','{','}','~','"','`','"'
                  ]
        print(text_list)
        for slovo in text_list:
            new_slovo = ''
            count_bykva = 1
            for part in slovo:
                if part not in errors:
                    new_slovo += part
            if new_slovo != '':
                if new_slovo not in freq_dict:
                    freq_dict[new_slovo] = count_bykva
                else:
                    count_bykva_new = freq_dict[new_slovo] + 1
                    freq_dict[new_slovo] = count_bykva_new
        #    count_bykva = texts_list.count(bykva)
    return  freq_dict

def filter_stop_words(freq_dict: dict, STOP_WORDS: tuple) -> dict:
    freq_dict_new = freq_dict.copy()
    if not  freq_dict or not STOP_WORDS:
        return  freq_dict
    if freq_dict != None or STOP_WORDS != None:
        return  freq_dict
    for new_stop_word in freq_dict.keys():
        if not isinstance(new_stop_word, str):
            freq_dict_new.pop(new_stop_word)
    for slovo_stop in STOP_WORDS:
        if slovo_stop in freq_dict_new:
            freq_dict_new.pop(slovo_stop)
    return freq_dict_new


def get_top_n(freq_dict_new: dict, top_n: int) -> tuple:
    top_my_list = []
    if top_n <= 0:
        return()
    else:
        for slovo_stop in freq_dict_new.keys():
            top_my_list.append(slovo_stop)
    tuple_top_n = tuple(top_my_list[:top_n])
    return (tuple_top_n)


#my_second_dict = sorted(my_second_dict.items(), key=lambda new_bykva: new_bykva[1], reverse=True)
#for key, value in my_second_dict.items():





