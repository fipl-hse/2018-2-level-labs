"""
Laboratory work 1
"""

def read_from_file(path_to_file, lines_limit) -> str:
    try:
        file = open(path_to_file, 'r')
    except FileNotFoundError:
        return None
    count = 0
    text = ''
    for i in file.read():
        if count == lines_limit:
            return text
        text += i
        count += 1
    file.close()
    return text


def calculate_frequences(text) -> dict:
    if text is None or str(text).isdigit():
        return {}
    trash = '''_-=!@#()~_+$%^&*]}{[:;'",./><?1234567890'''
    for i in text:
        if i in trash:
            text = text.replace(i, ' ')
    text_l = text.lower()
    text_split = text_l.split(' ')
    frequency = {}
    for i in text_split:
        if i not in frequency:
            frequency[i] = 1
        else:
            num = frequency.get(i)
            frequency[i] = num+1
            continue
    frequency_check = frequency.copy()
    for key in frequency_check.keys():
        if key == '' or '\n' in key:
            del frequency[key]
    return frequency


def filter_stop_words(frequency, stop_words) -> dict:
    if frequency is None or stop_words is None:
        return frequency
    frequency_copy = frequency.copy()
    frequency_iterate = frequency.copy()
    for key in frequency_iterate:
        if str(key).isdigit() or key in stop_words:
            del frequency_copy[key]
            continue
    return frequency_copy


def get_top_n(frequency_clean, top_n) -> tuple:
    if top_n < 0:
        return ()
    count = top_n
    top = []
    freq_list = []
    for key, value in frequency_clean.items():
        freq_list.append([key, value])
    for i in freq_list:
        if count == 0:
            break
        top.append(i[0])
        count -= 1
    top = tuple(top)
    return top


def write_in_file(path_to_report, top):
    file = open(path_to_report, 'w')
    for i in top:
        file.write(i)
        file.write('\n')
    file.close()
