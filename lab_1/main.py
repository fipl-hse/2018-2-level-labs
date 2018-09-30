"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text):
    freq_dict = {}

    if isinstance(text, str):
        text = text.lower()
        text.replace('\n', '')

        divided_text = text.split(" ")

        empty_word_list = []

        for word in divided_text:
            empty_word = ''

            if word.isalpha():
                empty_word_list.append(word)

            elif not word.isalpha():
                for letter in word:
                    if letter.isalpha():
                        empty_word += letter
            if empty_word:
                empty_word_list.append(empty_word)

        for word in empty_word_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        freq_dict_clean = freq_dict.copy()
        return freq_dict_clean
    else:
        return freq_dict


def filter_stop_words(freq_dict_clean, stopwords):

    if not freq_dict_clean or not stopwords:
        return freq_dict_clean

    for key in list(freq_dict_clean):
        if key in stopwords:
            del freq_dict_clean[key]
        if not isinstance(key, str):
            del freq_dict_clean[key]

    return freq_dict_clean


def get_top_n(freq_dict_clean, top_n):

    freq_list = []

    if not top_n > 0:
        return ()

    for k, value in freq_dict_clean.items():
        freq_list.append([value, k])

    top_freq_list = freq_list[:top_n]

    final_top_freq_list = []
    for element in top_freq_list:
        final_top_freq_list.append(element[1])

    final_top_freq_list = tuple(final_top_freq_list)

    return final_top_freq_list
