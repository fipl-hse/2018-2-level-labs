def read_from_file(path_to_file, lines_limit) -> str:
    f = open(path_to_file, 'r')
    count = 0
    text = ''
    for i in f.read():
        if count == lines_limit:
            return text
        else:
            text += i
            count += 1
    f.close()
    return text
    pass
    
    
def calculate_frequences(text) -> dict:
    punctuation = [',', '.', '<', '>', '/', '?', ';', ':', '*', '`', '~', '!',
                   '#', '$', '%', '^', '(', ')',
                   '-', '_', '@', '+', '=', '{', '[', '}', ']', '|', '"']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in str(text):
        if i in punctuation or i in numbers:
            text = text.replace(i, '')
    if text == None:
        return {}
    else:
        text_l = text.lower()
        text_split = text_l.split(' ')
        frequency = {}
        for i in text_split:
            if i not in frequency:
                frequency[i] = 1
            else:
                num = frequency.get(i)
                frequency[i] = num+1
    return frequency
    pass


def filter_stop_words(frequency, stop_words) -> dict:
    if frequency is None or stop_words is None:
        return frequency
    
    frequency_clean = frequency.copy()
    frequency_copy = frequency.copy()
    for i in frequency_copy:
        for n in stop_words:
            if i == n:
                del frequency_clean[i]
    return frequency_clean
    pass


def get_top_n(frequency_clean, top_n) -> tuple:
    if top_n < 0:
        return ()
    count = top_n
    top = []
    freq_list = list(frequency_clean.items())
    freq_sort = sorted(freq_list, key=lambda x: x[1], reverse=True)
    for i in freq_sort:
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
    pass
