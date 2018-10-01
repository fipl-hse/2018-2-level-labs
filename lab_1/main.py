"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def read_from_file(path_to_file: str, lines_limit: int) -> str:

    text = ""

    with open(path_to_file, encoding='utf-8') as f_text:
        for index, line in enumerate(f_text):
            if index < lines_limit:
                text += line
            else:
                break

    return text


def calculate_frequences(text: str) -> dict:

    freq_dict = {}

    if not text:
        return freq_dict

    if isinstance(text, str):
        words = text.lower().split(" ")
        if '' in words or '\n' in words:
            while '' in words:
                words.remove('')
            while '\n' in words:
                words.remove('\n')
        words_new = []

        for word in words:
            new_word = ""
            if not word.isalpha():
                for i in word:
                    if i.isalpha():
                        new_word += i
                if new_word:
                    words_new.append(new_word)
            else:
                words_new.append(word)

        for word in words_new:
            count_word = words_new.count(word)
            freq_dict[word] = count_word

    return freq_dict


def filter_stop_words(freq_dict: dict, stop_words: tuple) -> dict:

    if not freq_dict:
        return freq_dict

    freq_dict_new = freq_dict.copy()

    for key in freq_dict.keys():
        if not isinstance(key, str):
            freq_dict_new.pop(key)
    if stop_words:
        for word_stop in stop_words:
            if word_stop in freq_dict_new:
                freq_dict_new.pop(word_stop)

    return freq_dict_new


def get_top_n(freq_dict: dict, top_n: int) -> tuple:

    if not top_n > 0:
        return ()

    top_n_dict = sorted(freq_dict, key=freq_dict.__getitem__, reverse=True)
    return tuple(top_n_dict[:top_n])


def write_to_file(path_to_file: str, content: tuple):

    with open(path_to_file, "w", encoding='utf-8') as f_text:

        for word in content:
            word += '\n'
            f_text.write(word)
