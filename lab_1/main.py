"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
text = """hi"""
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

dictionary = calculate_frequences(text)
print (dictionary)

stop_words =('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about',
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
                  'it', 'how', 'further', 'was', 'here', 'than')

# def filter_stop_words(dictionary, stop_words) -> dict:
#     all_words = dictionary.keys()
#     #print(all_words)
#     clean_list = []
#     new_dictionary = {}
#     for name in all_words:
#         #print(name)
#         if name in stop_words:
#             all_words.pop(name)
#         else:
#             clean_list.append(name)
#          if name not in stop_words:
#             clean_keys = clean_list.append(name)
#         print(clean_list)
#          if name not in new_dictionary:
#              new_dictionary[name] = 0
#          new_dictionary[name] += 1
#              #return(new_dictionary)
#          print(new_dictionary)
#
# filter_stop_words(dictionary,stop_words)



#     """
#     Removes all stop words from the given frequencies dictionary
#     """
#     pass
#
# def get_top_n() -> tuple:
#     """
#     Takes first N popular words
#     """
#     pass
