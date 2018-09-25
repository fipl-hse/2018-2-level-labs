def calculate_frequences(text):
    """
    Calculates number of times each word appears in the text
    """
    dictionary = {}
    if text and not isinstance(text, int):
        text = text.lower()
        text.replace('\n', ' ')
        list_text = text.split(' ')
        while text.find('  ') != -1:
            text = text.replace('  ', '')
        while '\n' in list_text:
            list_text.remove('\n')
        symbols = '''!@#$%^&*()"№:?,.<>/'[]{};-+~`1234567890\n'''
        print(list_text)
        for word in list_text:
            new_word = ''
            count = 1
            for sign in word:
                if sign not in symbols:
                    new_word += sign
            if new_word != '':
                if new_word not in dictionary:
                    dictionary[new_word] = count
                else:
                    new_count = dictionary[new_word] + 1
                    dictionary[new_word] = new_count

    return dictionary


def filter_stop_words(freq_dict, stop_words) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """

    if not freq_dict:
        return freq_dict
    new_freq_dict = freq_dict.copy()
    all_words = freq_dict.keys()
    for name in all_words:
        if not isinstance(name, str):
            new_freq_dict.pop(name)
    if not stop_words:
        return freq_dict
    for word in stop_words:
        if word in new_freq_dict:
            new_freq_dict.pop(word)
    return new_freq_dict


def get_top_n(frequencies: dict, top_n: int) -> tuple:
        
    top_list = []
    if top_n <= 0:
        return()
    all_words = frequencies.keys()
    for word in all_words:
        top_list.append(word)
    tuple_top_n = tuple(top_list[:top_n])
    return tuple_top_n

