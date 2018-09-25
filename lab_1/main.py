"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
frequency = {}


def count_frequency(base):
    words = base.split(' ')
    frequency_dict = {}
    if type(base) is str:
        for i in range(0, len(words)):
            frequency_dict[words[i]] = words.count(words[i])

    return frequency_dict


pass


def filter_stop_words(new_dict, stop_words):
    freq = {key: new_dict[key] for key in new_dict if (key not in stop_words) and (type(key) is str)}
    right_words = sorted(freq, key=freq.get)
    right_words.reverse()
    return right_words


pass


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
wrong_words = ['usually', 'have', 'my']
first_dict = count_frequency(text)
filtered = filter_stop_words(first_dict, wrong_words)
N = int(input('enter an appropriate n, please'))
finish = get_top_n(filtered, N)
