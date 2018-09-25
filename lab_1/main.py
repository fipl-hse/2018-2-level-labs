#Not works
"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:

    freq_dict = {}
    if text is None or str(text).isdigit():                                      
        freq_dict = {}
        return freq_dict

def filter_stop_words(freq_dict: dict, STOP_WORDS: tuple) -> dict:

    errors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  '!', '?', '.', ',', '_', '-', '@', '#', '$', '&',
                  '^', '%', '*', '=', '-', '+', '/', ']', '[',
                  '>', '<', ':', ';', '{', '}', '~', '"', '`', '"'
                  ]                                                                
    for slovo in text:
        if slovo in errors:
            text = text.replace(slovo, ' ')
            continue

    text = text.lower()
    text = text.split(' ')
                                                                    
    for slovo_new in text:
        freq_slovo = text.count(slovo_new)
        freq_dict[slovo_new] = freq_slovo
        continue

    return freq_dict


#def filter_stop_words(freq_dict: dict, STOP_WORDS: tuple) -> dict:

    if freq_dict is None or STOP_WORDS is None:                                        
        return freq_dict

    for key in list(freq_dict):                                                       
         if str(key).isdigit() or key in STOP_WORDS:
             freq_dict.pop(key)
      
    return freq_dict


def get_top_n(freq_dict_new: dict, top_n: int) -> tuple:

    if top_n < 0:                                                                    
        return ()

    top_my_list = []                                            
    for key, value in freq_dict_new.items():
        top_my_list.append([value, key])
        continue

    sorted(top_my_list, reverse = True)                        

    itog_list = []                                              
    count_itog = top_n
    for thing in top_my_list:
        if count_itog == 0:
            break
        itog_list.append(thing[1])
        count_itog -= 1
    tuple_top_n = tuple(itog_list)
    return tuple_top_n
