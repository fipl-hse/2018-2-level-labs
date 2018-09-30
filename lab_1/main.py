"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

from collections import Counter
def calculate_frequences(text:str)-> dict:
    v = {}
    if type(text) == str:
        text = text.lower()
        t = []
        marks_and_numbers = """['0','1','2','3','4','5','6','7','8','9','.',','!',','?',
        ':',';','\','/','"','*','-','_',''','"','@','#','$','%','^','&','(',')','+','=',
        '[',']','{','}','~','<','>','№' ]"""
        for m_n in marks_and_numbers:
            if m_n in text:
                text = text.replace(m_n,' ')
        t = text.split()
        number = len(t)
        for i in t:
            if v.get(i):
                v[i] += 1      
            else: 
                v[i] = 1
    elif text == None or type(text) != str:
        return v         
    return v


def filter_stop_words(v:dict,stop_words:tuple)-> dict:
    if not(isinstance(v,dict)):
        return {}
    if not(isinstance(stop_words,tuple)):
        return v
    del_list = []
    for key in v.keys():
        if key in stop_words:
            del_list.append(key)
        if not(isinstance(key,str)):
            del_list.append(key)
    
    for element in del_list:
        v.pop(element)
 
    return v
    

def get_top_n(v:dict,n:int)-> tuple:
    v_sort = Counter(v).most_common()
    print('v_s = ', v_sort)
    top_n = v_sort[:n]
    print('TOP_N = ',top_n)
    temp_list = []
    for temp in top_n:
        temp_list.append(temp[0])

    return(tuple(temp_list))

