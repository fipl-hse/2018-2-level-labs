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
    if text == None or text.isdigit():
        return {}
    trash = '''_-=!@#()~_+$%^&*]}{[:;'",./><?1234567890'''
    for i in text:
        if i in trash:
            text = text.replace(i, ' ')
    text_l = text.lower()
    text_split = text_l.split(' ')
    frequency = {}
    for i in text_split:
         freq_word = text.count(i)
         frequency[i] = freq_word
         continue
    return frequency
    pass


def filter_stop_words(frequency, stop_words) -> dict:
    if frequency is None or stop_words is None:
        return frequency
    frequency = list(frequency)
    frequency_copy = frequency.copy()
    for key in frequency_copy:
         if str(key).isdigit() or key in stop_words:
             frequency_copy.pop(key)
             continue
     return frequency_copy
     pass


def get_top_n(frequency_clean, top_n) -> tuple:
    if top_n < 0:
        return ()
    count = top_n
    top = []
    freq_list = []
    for key, value in frequency.items():
        list.append([key, value])
    freq_sort = sorted(freq_list, reverse=True)
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
    pass
