dict_freq = {}
def calculate_frequences(text) -> dict:
    
    clean_text = []
    clean_str = ''
       
    if type(text) != str:
        return {}
    
    low_text = text.lower()
    a = low_text.split(" ")
    for i in a:
        if type(i) != str:
            return {}
        for s in i:
            if not s.isalpha():
                pass
            else:
                clean_str.replace('', s)
                clean_text.append(clean_str)
                clean_str = ''
        
    if clean_text == []:
        return {}
    else:
        for i in clean_text:
            dict_freq[i]= clean_text.count([i])   
    
    return dict_freq

def filter_stop_words(dict_freq: dict, stop_words: tuple) -> dict:
    list_from_dict_with_values = []
    
    
    if stop_words == None:
        return dict_freq
    else:
        list_stop_words = list(stop_words)
        for i in list_stop_words: 
            if type(i) != str:
                return {}

    
    
    if dict_freq == None:
        return {}
    else:
        for key in dict_freq.keys():
            if type(key) != str:
                return {}

        list_from_dict = list(dict_freq)
        for i in list_from_dict:
            if type(i) != str:
                return {}
        
    for value in dict_freq.values():
        list_from_dict_with_values.append(value)

    

    for i, e in enumerate(list_from_dict):
        if e == None:
            return {} 
        if e in list_stop_words:
            list_from_dict.remove(e)
            del list_from_dict_with_values[i]
    
    dict_without_stop_words = dict(zip(list_from_dict, list_from_dict_with_values))
    return dict_without_stop_words
    



def get_top_n(dict_without_stop_words: dict, n: int) -> tuple:
    sorted_and_reversed_list = []
    list_with_max = []
    new_list = []
    if type(n) != int:
        return()
        
    for value in dict_without_stop_words.values():
        sorted_and_reversed_list.append(value)
        sorted_and_reversed_list.sort(reverse = True)

    for i in sorted_and_reversed_list:
        for key, value in dict_without_stop_words.items():
            if value == i:
                list_with_max.append(key)
                dict_without_stop_words[key] = ''
                break
    if n > len(sorted_and_reversed_list):
        return tuple(list_with_max)
    if n < 0:
        return()
    
    list_with_n_max = list_with_max[: n]
    tuple_with_max = tuple(list_with_n_max)
    return tuple_with_max
  
