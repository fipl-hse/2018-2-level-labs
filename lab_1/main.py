"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
TEXT = '''The Internet was invented in the late 1960s by the US Defense
Department’s Advanced Research Projects Agency. A mainframe computer is a
large, powerful computer, shared by many users. The idea of the electronic
mailbox was born when users looked for a way to talk to each other electronically.
By 1984,the Internet had begun to develop into the form we know today.'''

FREQ_DICT = {}
STOP_WORDS = ('large', 'way', 'just', 'to', 'when', 'other', 'mainframe', 'us', 'today',
              'form', 'develop', 'know', 'a', 'each', 'talk', 'looked', 'invented')
FINISH_LIST = []

def calculate_frequences(TEXT) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if not isinstance(TEXT, str):  # если текст не текст, то не надо его
        return {}

    text_l = TEXT.lower()
    punct = '''.,!?;:'"<>/\[]{}()1234567890*-+$%@#&^~`'''  # знаки препинания для исключения из текста
    punct = list(punct)
    for i in punct:
        text_l = text_l.replace(i, ' ') #заменяем знаки препинания на пробелы

    text_s = text_l.split()             #превращаем обработанный текст в список
    text_u = []                        # создаем список для слов без повторов
    for i in text_s:                    # и его заполняем 
        if not i in text_u:
            text_u.append(i)

    text_f = []                      #а это список для частот слов в исх.тексте
    for i in text_u:                # слова берем из списка без повторов
        text_f.append(text_s.count(i))
    FREQ_DICT = dict(zip(text_u, text_f))  
    return FREQ_DICT


def filter_stop_words(FREQ_DICT, STOP_WORDS) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    filtered_dict = {}
    if (FREQ_DICT is None or STOP_WORDS is None or FREQ_DICT == {}):
        return{}

    if STOP_WORDS == ():
        return FREQ_DICT

    STOP_WORDS = (STOP_WORDS + (1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
    sw_l = list(STOP_WORDS)

    for i in FREQ_DICT.keys():
        if not i in sw_l:
            filtered_dict[i] = FREQ_DICT[i]

    return filtered_dict 


def get_top_n(filtered_dict, top_n) -> tuple:
    """
    Takes first N popular words
    """ 

    FINISH_LIST = filtered_dict.values()
    FINISH_LIST = list(FINISH_LIST)
    FINISH_LIST = sorted(FINISH_LIST)

    if top_n > len(FINISH_LIST):
        top_n = len(FINISH_LIST)

    popular = []
    for k in range(top_n):
        i = FINISH_LIST[-(k+1)]
        for key, value in filtered_dict.items():
            if value == i:
                popular.append(key)
    popular = popular[0:top_n]
    popular = tuple(popular)
    return popular
