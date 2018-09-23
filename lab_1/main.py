import re
from string import punctuation
from collections import Counter
r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
def filter_stop_words(x):
    if len(x) <= 3:
        return False
    else:
        return True

def get_top_n():
    file = open("texte.txt", "r")
    dbfile = file.read()
    dbfile = r.split(dbfile)
    calculate_frequences()

def calculate_frequences():
    top = int(input('top what?'))
    words = []
    file = open("texte.txt", "r")
    dbfile = file.read()
    dbfile = r.split(dbfile)
    stopwords1 = dbfile
    swfilter = filter(filter_stop_words, stopwords1)
    for x in swfilter:
        words.append(x)
    words = [y for y in words if not (y.isdigit() 
                                         or y[0] == '-' and y[1:].isdigit())]
    #print (words)
    freqfin = []
    words = (Counter(words).most_common(top))
    freqfin = [str(z) for z in words]
    freqfin = [z + '\n' for z in freqfin]
    freqfin = ''.join(freqfin)
    freqtop = open("frequency.txt", "w")
    freqtop.writelines (freqfin)
    print (freqfin)
get_top_n()
