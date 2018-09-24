"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
text = "The quick brown fox jumps over the lazy dog"
import re

# re.sub(r'\s', '', text)
def calculate_frequences(text):
    dictionary = {}
    if text and type(text) != int:
        text = text.lower()
        text.replace('\n', ' ')

        for element in '1234567890':
            text = text.replace(element, '')
            list_text = text.split(' ')

        text.strip(' ')
        while text.find('  ') != -1:
            text = text.replace('  ', '')
        while '\n' in list_text:
            list.text.remove('\n')

        list_text = text.split(' ')
        symbols = '''!@#$%^&*()"№:?,.<>/'[]{};-+~`1234567890\n'''

        for word in list_text:
            for sign in word:
                if sign in symbols:
                    word = word.replace(sign, '')
            if word not in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1
        return(dictionary)
    else:
        return(dictionary)




def filter_stop_words(freq_dict,stop_words) -> dict:
    freq_dict = {}
    if not freq_dict:
        return freq_dict
    new_freq_dict = freq_dict.copy()
    all_words = freq_dict.keys()
    for name in all_words:
        if name != str:
            new_freq_dict.pop(name)
    if stop_words:
        if word in stop_words:
            new_freq_dict.pop(word)
    return new_freq_dict



#     """
#     Removes all stop words from the given frequencies dictionary
#     """
#     pass
def get_top_n(frequencies: dict, top_n: int) -> tuple:
    top_tuple = ()
    if top_n <= 0:
        return top_tuple
    else:
        all_words = frequencies.keys()
        for word in all_words:
            top_list.append(word)
    tuple_top_n = tuple(top_list[:top_n])
    print (tuple_top_n)




# def get_top_n() -> tuple:
#     """
#     Takes first N popular words
#     """
#     pass
