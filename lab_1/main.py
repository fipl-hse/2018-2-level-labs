"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text) -> dict:
    frequent_dict = {}
    import re
    if text and type(text) != int:
        prepared_text = re.findall(r'[a-z]+', text.lower())
        print(prepared_text)
        for index, element in enumerate(prepared_text):
            new_word = ''
            count = 1
            for el_index in range(len(element)):
                if element[el_index] in 'qwertyuioplkjhgfdsazxcvbnm':
                    new_word += element[el_index]
            if new_word not in frequent_dict:
                frequent_dict[new_word] = count
            else:
                new_count = frequent_dict[new_word] + 1
                frequent_dict[new_word] = new_count
        return frequent_dict
    else:
        return frequent_dict

def filter_stop_words(frequent_dict, stop_words) -> dict: #Removes all stop words from the given frequencies dictionary
    new_frequent_dict = {}
    for word, frequency in frequent_dict.items():
        if word not in stop_words:
            new_frequent_dict[word] = frequency
    return new_frequent_dict

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass

text = '''The the the the
semantic field of any town is an associations of people. For the N.V. Podolskaya in “The Dictionary of Russian
Onomastic Terminology”. 
any system of onyms is characterized with a number of features.'''
stop_words = ['onomastics', 'the', 'onym']
frequent_dict = calculate_frequences(text)
frequent_dict = filter_stop_words(frequent_dict, stop_words)
# get_top_n(frequent_dict, n)
print(frequent_dict)
