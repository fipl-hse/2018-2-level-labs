import re
from string import punctuation
from collections import Counter

r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
stpw = []
stpw = ['a', 'an', 'is', 'are', 'am', 'the', 'of', 'with', 'at', 'to', 'in']
def text_input():
    global words
    words = str(input("Put your text here, please: "))
    secret = '.txt'
    bull = int(words.find(secret))
    if int(bull) == int(len(words) - 4):
        text = open(words, 'r')
        text = text.read()
        words = text
        words = str(words.lower())
        return words
        return True
        calculate_frequences()
    else:
        words = str(words.lower())
        calculate_frequences()
        return words
        return False
    pass

def calculate_frequences() -> dict:
    global words
    words1 = r.split(words)
    global freq
    freq = (Counter(words1).most_common())
    freq = dict(freq)
    return freq
    pass

def filter_stop_words() -> dict:
    global filtered_words
    
    #filtered_words = {y: freq[y] for y in freq if not (y.isdigit()
                                            #or freq[0] == '-' and freq[1:].isdigit())}
    filtered_words = {k: freq[k] for k in freq if k not in stpw}
    return filtered_words
    pass


def get_top_n() -> tuple:
    global fin
    top = int(input("Enter the number for top n: "))
    fin = tuple(Counter(filtered_words).most_common(top))
    for i in fin:
        print(i)
    return fin
    pass
def file_output():
    final = list(fin)
    file = str(input('Enter the name of the file (with .txt): '))
    out = open(file, 'w')
    for z in final:
        out.write(str(z))
        out.write('\n')
        print (z)
    out.close()
    pass
    
