"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
frequency = {}


def calculate_frequences(base):
    frequency_dict = {}
    if type(base) is str:
        base = base.lower()
        signs = "?!%~<>/\.,[]{}()@"'#*&0123456789"
        for c in sings:
            base = base.replase(c," ")
        base1 = base.lower()
         
        for i in range(0, len(base1)):
            frequency_dict[base1[i]] = base1.count(base1[i])

    return frequency_dict



def filter_stop_words(new_dict, stop_words):
    filtered_words = {}
    
    if not stop_words:
        stop_words = tuple()
    if new_dict:
        filtered_words = {key: new_dict[key] for key in new_dict if (key not in wrong_words) and (type(key)  is str)}
        
    return filtered_words
        
  



def get_top_n(right_words, top_n: int):
    final = ''
    for i in range(top_n):
        final += right_words[i]
        final += '\n'
    return final


pass

text = '''I always have lunch at 7:00 evenings.
          My friends and I usually have fun together.
          365 members of my family are very close to me,
          my father is so smart.'''
text = text.lower()
wrong_words = ('usually', 'have', 'my')
first_dict = calculate_frequencies(text)
filtered = filter_stop_words(first_dict, wrong_words)
#N = int(input('enter an appropriate n, please'))
N = 2
finish = get_top_n(filtered, N)
