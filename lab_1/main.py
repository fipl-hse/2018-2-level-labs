
#Labour work #1
def calculate_frequences() -> dict:
    text = re.sub(r'[^\w\s]+|[\d]+','', text)
    text = text.lower()
    text = text.split()
    counted_words = {}
    current_word = []
    for current_word in text:
        value =  text.count(current_word)  # берет эл-т из списка и считает сколько раз этот эл=т встр в этом списке
        counted_words[current_word] = value # на каждом шагу по этому циклу запишет в ключ сколько это слов употребл в тексте
    return {}

def filter_stop_words() -> dict:
   counted_words_new = counted_words.copy()

    for current_word in list(counted_words_new):# словарь переводим в список, эл-т в спискее=ключ
        if current_word in stop_words:# current word = key
            counted_words_new.pop(current_word)
    return counted_words_new
    pass

def get_top_n() -> tuple:
   counted_words_new = sorted(counted_words_new.items(), key = lambda i:i[1], reverse=True)
    counter  = 0
    lists = []
    for key in counted_words_new:
        if counter == top_n:
            break
        else: 
            lists.append(key[0])
            counter  +=1
            continue
    return tuple(lists)
    pass
