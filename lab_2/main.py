

"""
Labour work #2
 Check spelling of words in the given text"""
def calculate_frequencies(text: str) -> dict:
    first_dict = {}
    list_of_marks = [
                    '.', ',', ':', '"', '`', '[', ']',
                    '?', '!', '@', '&', "'", '-',
                    '$', '^', '*', '(', ')',
                    '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                    ]
    try:
        elements = text.split()
    except AttributeError:
        return first_dict
    for thing in elements:
        if thing.isdigit():
            continue
        for mark in list_of_marks:
            if mark in thing:
                pos_mark = thing.find(mark)
                thing = thing[:pos_mark] + thing[pos_mark + 1:]
            thing = thing.strip(mark)
        thing = thing.lower()
        first_dict[thing] = first_dict.get(thing, 0) + 1
    if '' in first_dict.keys():
        first_dict.pop('')
    return first_dict
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCT_MARKS = ['.', ',', '"', ':', ';', '-', '"', '"', '?', ''', ''']
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequencies(REFERENCE_TEXT)
candidates = []
lst1 = []
lst2 = []
lst3 = []
lst4 = []
if __name__ == '__main__':
    with open('migrants.txt', 'r') as g:
        MY_TEXT = g.read()
print(MY_TEXT)
WTEXT = MY_TEXT
WTEXT = list(WTEXT)
for i in range(0, len(WTEXT)):
    if (WTEXT[i].isalpha() and not WTEXT[i+1].isalpha() and not WTEXT[i+1] == " ") or (not WTEXT[i].isalpha() and not WTEXT[i+1].isalpha() and not WTEXT[i] == " "):
        WTEXT.insert(i+1, " ")
WTEXT = ''.join(WTEXT)
WTEXT = WTEXT.split(" ")
print(WTEXT)
for i in range(0, len(WTEXT)):
    if WTEXT == '':
       WTEXT.remove(WTEXT[i])
for item in WTEXT:
    if item.isalpha():
       lst1 = ((item + " ")*len(item)).split(" ")
       lst1.remove(lst1[-1])
       for i in range(0, len(lst1)):
           lst1[i] = lst1[i].replace(lst1[i][i], '')
           candidates.append(lst1[i])
       lst2 = ((item + " ")*(len(item)-1)).split(" ")
       lst2.remove(lst2[-1])
       for k in range(0, len(lst2)):
           lst2[k] = list(lst2[k])
       for k in range(0, len(lst2)):
           lst2[k][k] = item[k+1]
           lst2[k][k+1] = item[k]
           lst2[k] = ''.join(lst2[k])
           candidates.append(lst2[k])
       for j in range(0, len(LETTERS)):
           for i in range(0, len(item)+1):
               word = list(item)
               word.insert(i, " ")
               lst3.append(word)
               for k in range(0, len(lst3)):
                   lst3[k] = ''.join(lst3[k])
                   lst3[k] = lst3[k].replace(" ", LETTERS[j])
                   candidates.append(lst3[k])
           for i in range(0, len(item)):
                word = list(item)
                word[i] = " "
                lst4.append(word)
                for l in range(0,len(lst4)):
                    lst4[l] = ''.join(lst4[l])
                    lst4[l] = lst4[l].replace(" ", LETTERS[j])
                    candidates.append(lst4[l])
       can1 = list(filter(lambda x: candidates.count(x) == 1, candidates))
       can2 =[]
       for c in candidates:
           if candidates.count(c) > 1:
              if c in can2:
                 continue
              else:
                  can2.append(c)
       candidates += (can1 + can2)
    else:
        continue
print(candidates)

