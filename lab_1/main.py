"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    unrelevant_symbols_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '`', "'", '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '"',
                               '№', ';', ':', '?', '-', '=', '/', '\n', '\t', '|', '<', '>', '"', '[', ']', '{', '}']
    freq_dict = {}

    if text is None or text == '':
        return freq_dict
    else:
        text = text.lower()

        for lett in text:
            if lett.isalpha():
                continue
            else:
                for s in unrelevant_symbols_list:
                    if s == lett:
                        text = text.replace(lett, '')

        text = text.split(' ')
        text_copy = text[:]
        for word in text_copy:
            if word == '':
                continue
            else:
                text += word

        for word in text:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
    freq_dict_clean = freq_dict.copy()
    return freq_dict, freq_dict_clean


def filter_stop_words(freq_dict_clean, stopwords):
    print(freq_dict_clean)

    for key in list(freq_dict_clean):
        if key in stopwords:
            del freq_dict_clean[key]

    return freq_dict_clean


def get_top_n(freq_dict_clean, top_n):
    freq_list = []

    for k, v in freq_dict_clean.items():
        freq_list.append([v, k])
    print(freq_list)
    freq_list.sort(reverse=True)

    top_freq_list = freq_list[:top_n]

    final_top_freq_list = []
    for i, element in enumerate(top_freq_list):
        final_top_freq_list.append(element[1])

    final_top_freq_list = tuple(final_top_freq_list)

    return final_top_freq_list


