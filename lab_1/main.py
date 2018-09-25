dict_freq = {}
def calculate_frequences(text) -> dict:
    
    clean_text = []
    clean_str = ''
       
    if type(text) != str:
        return{}
    
    low_text = text.lower()
    a = low_text.split(" ")
    for i in a:
        for s in i:
            if s.isalpha():
                clean_str += s
        clean_text.append(clean_str)
        clean_str = ''
                  
    for i in clean_text:
        dict_freq[i] = clean_text.count(i)   
    
    return dict_freq

def filter_stop_words(dict_freq: dict, stop_words: tuple) -> dict:

    for i in stop_words: 
        if type(i) != str:
            stop_words.remove(i)  

    list_from_dict = list(dict_freq)
    for value in dict_freq.values():
        list_from_dict_with_values.append(value)

    

    for i, e in enumerate(list_from_dict):
        if e in stop_words:
            list_from_dict.remove(e)
            del list_from_dict_with_values[i]
    
    dict_without_stop_words = dict(zip(list_from_dict, list_from_dict_with_values))
    return dict_without_stop_words
    


sorted_and_reversed_list = []
list_with_max = []

def get_top_n(dict_without_stop_words: dict, n: int) -> tuple:
   
    if type(n) != int:
        return()
        
    for value in dict_without_stop_words.values():
        sorted_and_reversed_list.append(value)
        sorted_and_reversed_list.sort()
        sorted_and_reversed_list.reverse()

    for i in sorted_and_reversed_list:
        for key, value in dict_without_stop_words.items():
            if value == i:
                list_with_max.append(key)
                del dict_without_stop_words[key]
                break
    
    list_with_n_max = list_with_max[1 : n+1 : 1]
    tuple_with_max = tuple(list_with_n_max)
    return tuple_with_max
  
