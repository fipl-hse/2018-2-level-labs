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

def filter_stop_words(v,stop_words):
    del_list = []
    for key in v.keys():
        if key in stop_words:
            del_list.append(key)
    print(v)
    
    for element in del_list:
        v.pop(element)
    print(v)

def get_top_n(v,n):
    v_sort = Counter(v).most_common()
    top_n = v_sort[:n]
    print('TOP_N = ',top_n)
    
text = input('Введите текст: ')
v = count_words(text)
stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about',
              'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be',
              'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself',
              'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
              'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should',
              'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',
              'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in',
              'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
              'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has',
              'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
              'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing',
              'it', 'how', 'further', 'was', 'here', 'than']
              
filter_words(v,stop_words)
n = int(input('Введите n = ')) # есои n не число

get_top_n(v,n)
