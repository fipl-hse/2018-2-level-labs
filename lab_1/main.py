import string


def calculate_frequences(text: str) -> dict:
    
    if text == "" or text is None or type(text) != str:
        return {}

    words = text.split()
    dict_freq = {}
    
    for word in words:
        word = word.lower()
        
        for i in string.punctuation:
            word = word.replace(i, '')
            
        if word == "":
            continue
        if word.isdigit():
            continue

        if dict_freq.get(word) == None:
            dict_freq[word] = 1
        else:
            dict_freq.update({word: dict_freq[word] + 1})
            
            
    return dict_freq


def filter_stop_words(frequences: dict, stop_words: tuple) -> dict:
    
    if frequences is None and stop_words is None:
        return {}
    
    if stop_words == () or frequences == {}:
        return frequences
    
    if stop_words is None or frequences is None:
        return frequences
    
    new_frequences = {}
    for word in frequences:
        if type(word) == str:
            new_frequences[word] = frequences[word]
    frequences = new_frequences
    
    for stop_word in stop_words:
        if type(stop_word) != str:
            continue
        else:
            frequences.pop(stop_word, '')
            
            
    return frequences


def get_top_n(frequences: dict, top_n: int) -> tuple:
    
    if frequences == {} or top_n <= 0:
        return ()
    top_words = []
    n = 0
    
    for word in frequences:
        if n == top_n:
            break
        top_words.append(word)
        n += 1
        
    return tuple(top_words)
