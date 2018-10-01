
"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text):
    frequency_dict = {}
    if isinstance(text, str):
        text1 = text.lower()
        signs = """^;:$`?№!%~<>/\.,[]{}()@"'#*&0123456789"""
        for c in signs:
            text1 = text1.replace(c, " ")

        clean_text = text1.split()

        for i in range(0, len(clean_text)):
            frequency_dict[clean_text[i]] = clean_text.count(clean_text[i])
    return frequency_dict


def filter_stop_words(new_dict, stop_words):
    filtered_words = {}
    if not stop_words:
        stop_words = tuple()
    if new_dict:
        filtered_words = {key: new_dict[key] for key in new_dict if (key not in stop_words) and (type(key) is str)}
    return filtered_words




def get_top_n(new_dict, top_n: int):
    filtered_list = sorted(new_dict.items(), key=lambda item: item[1], reverse=True)
    if top_n > len(filtered_list):
        top_n = len(filtered_list)
    final_words = tuple(filtered_list[i][0] for i in range(top_n))
    return final_words
