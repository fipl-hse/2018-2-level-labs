

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
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
PUNCT_MARKS = ['.', ',', '"', ':', ';', '-', '"', '"', '?', ''', ''']
REFERENCE_TEXT = ''
if __name__=='__main__':
   with open('very_big_reference_text','r')as f:
        REFERENCE_TEXT = f.read()
item = 'cat'
as_is_words = ("CTA", )
freq_dict = calculate_frequencies(REFERENCE_TEXT)
depth_permutations = 1
def propose_candidates(item: str, depth_permutations: int = 1) -> list:
    candidates = list()
    if item == None or item == " " or item == '' or depth_permutations == 'None' or type(depth_permutations) != int or depth_permutations <= 0:
       candidates == []
    else:
       lst1 = []
       lst2 = []
       lst3 = []
       lst4 = []
       lst1 = ((item + " ") * len(item)).split(" ")
       lst1.remove(lst1[-1])
       for i in range(0, len(lst1)):
           lst1[i] = lst1[i].replace(lst1[i][i], '')
           candidates.append(lst1[i])
       lst2 = ((item + " ") * (len(item) - 1)).split(" ")
       lst2.remove(lst2[-1])
       for k in range(0, len(lst2)):
           lst2[k] = list(lst2[k])
           lst2[k][k] = item[k + 1]
           lst2[k][k + 1] = item[k]
           lst2[k] = ''.join(lst2[k])
           candidates.append(lst2[k])
       for j in range(0, len(LETTERS)):
           for i in range(0, len(item) + 1):
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
           for l in range(0, len(lst4)):
               lst4[l] = ''.join(lst4[l])
               lst4[l] = lst4[l].replace(" ", LETTERS[j])
               candidates.append(lst4[l])
       can1 = list(filter(lambda x: candidates.count(x) == 1, candidates))
       can2 = []
       for c in candidates:
           if candidates.count(c) > 1 and c in can2 or c in can1:
              continue
           else:
              can2.append(c)
       candidates = can1 + can2
    return candidates
def keep_known(candidates, freq_dict):
    known = list()
    if candidates == () or candidates is None or type(candidates) != tuple or freq_dict == '' or freq_dict is None:
       known = []
    else:
       known = list(filter(lambda x: type(x) == str and x in freq_dict.keys(), candidates))
    return known
def choose_best(freq_dict,candidates) ->str:
    best = str()
    if freq_dict == dict() or freq_dict is None or candidates == tuple() or candidates is None:
       best = 'UNK'
    else:
       values = []
       for c in candidates:
           if c in freq_dict and type(c) == str:
              values.append(freq_dict[c])
       maxi = max(values)
       most_freq = list(filter(lambda x: x in freq_dict and type(x) == str and freq_dict[x] == maxi, freq_dict))
       if len(most_freq) == 1:
          best = most_freq[0]
       else:
          lens = []
          for i in range(0, len(most_freq)-2):
              lens.append(len(most_freq[i]))
          for i in range(0, len(most_freq)-1):
              for k in range(0, maxi):
                  if k > len(most_freq[i]):
                     most_freq.remove(most_freq[i])
                  if LETTERS.index(most_freq[i][k]) > LETTERS.index(most_freq[i+1][k]):
                     most_freq.remove(most_freq[i])
                  elif LETTERS.index(most_freq[i][k]) < LETTERS.index(most_freq[i+1][k]):
                     most_freq.remove(most_freq[i+1])
                  else:
                     continue
          most_freq = most_freq[:]
          best = most_freq[0]
    return best
def spell_check_word(freq_dict, as_is_words, item):
    if item is None or freq_dict is None:
       final = 'UNK'
    else:
        if as_is_words is not None and item in as_is_words or item in freq_dict.keys():
           final = item
        else:
           candidates = propose_candidates(item, depth_permutations)
           known = keep_known(candidates, freq_dict)
           final = choose_best(freq_dict, candidates)
    return final
