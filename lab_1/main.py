"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
text = '''The Internet was invented in the late 1960s by the US Defense
Department’s Advanced Research Projects Agency. A mainframe computer is a
large, powerful computer, shared by many users. The idea of the electronic
mailbox was born when users looked for a way to talk to each other electronically.
By 1984,the Internet had begun to develop into the form we know today.'''

freq = {}
fsw = {}
stop_words = ('large', 'way', 'just', 'to', 'when', 'other', 'mainframe', 'us', 'today',
              'form', 'develop', 'know', 'a', 'each', 'talk', 'looked', 'invented')
l=[ ]

def calculate_frequences(text) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if not isinstance(text, str):  # если текст не текст, то не надо его
        return {}

    text_l = text.lower()
    
    punct = '''.,!?;:'"<>/\[]{}()1234567890*-+$%@#&^~`''' #знаки препинания для исключения из текста
    punct = list(punct)
    for i in punct:
        text_l = text_l.replace(i, ' ') #заменяем знаки препинания на пробелы

    text_s = text_l.split()             #превращаем обработанный текст в список
    text_u = [ ]                        # создаем список для слов без повторов
    for i in text_s:                    # и его заполняем 
        if not i in text_u:
            text_u.append(i)

    text_f=[ ]                      #а это список для частот слов в исх.тексте
    for i in text_u:                # слова берем из списка без повторов
        text_f.append(text_s.count(i))
    freq = dict(zip(text_u, text_f))
  
    return freq

def filter_stop_words(freq_dict, stop_words) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    if (freq_dict is None or stop_words is None or freq_dict == {}):
        return{}

    if stop_words == ():
        return freq_dict

    stop_words = (stop_words + (1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
    sw_l = list(stop_words)

    for i in freq_dict.keys():
        if not i in sw_l:
            filtered_dict[i] = freq_dict[i]

    return filtered_dict

def get_top_n(filtered_dict, top_n) -> tuple:
    """
    Takes first N popular words
    """
        

    l = filtered_dict.values()
    l = list(l)
    l = sorted(l)

    if top_n > len(l):
        top_n = len(l)

    popular = [ ]
    for k in range(top_n):
        i = l[-(k+1)]
        for key, value in filtered_dict.items():
            if value == i:
                popular.append(key)
    popular = popular[0:top_n]
    popular = tuple(popular)
    return popular


    # Вот пошла программа

    print ("Это частоты по всем словам.")
    f = calculate_frequences(text)
    for key, value in f.items():
            print (key, " ", value)

    print (" ")        
    print ("Это частоты слов, за исключением стопов.")    
    ff = filter_stop_words (f, stop_words)    
    for key, value in filtered_dict.items():
            print (key, " ", value)

    top_n = 3
    fff = get_top_n(filtered_dict, top_n)
    print (" ")
    print ("Это самые популярные слова.") 
    print (fff)


