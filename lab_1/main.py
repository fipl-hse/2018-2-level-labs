"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text):
    text = text.lower()
    t = []
    punctuation_marks = """['.',','!',','?',':',';','\','/','"','*',
    '-','_',''','"','@','#','$','%','^','&','(',')','+','=','[',']',
    '{','}','~','<','>','№' ]"""
    for p_m in punctuation_marks:
        if p_m in text:
            text = text.replace(p_m,' ')
    t = text.split()
    number = len(t)
    v = {}
    for i in t:
        if v.get(i):
            v[i] += 1      
        else: 
            v[i] = 1
    
    print(v)
    return v

def filter_stop_words() -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    pass

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
