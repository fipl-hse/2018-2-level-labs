def read_from_file(path_to_file, lines_limit):
    a = open(path_to_file, 'r')
    x = 0
    text = '' 
    for i in a.read():
        if x == lines_limit:
            return text
        else:
            text += i
            x += i
            a.close()
    return text


def calculate_frequences(text):
    if text == None or str(text).isdigit():
        return {}
    punct_numb = ''',<>./"'?:;}{[]!@(#$%^&*+-|№~`–_—)1234567890'''
    for i in text:
        if i in punct_numb:
            text = text.replace(i, '')
    text_down = text.lower()
    text_list = text_down.split(' ')
    frequency = dict()
    for i in text_list:
        if i not in frequency:
            frequency[i] = 1
        else:
            count = frequency.get(i)
            frequency[i] = count+1
        continue       
    frequency_second = frequency.copy()
    for key in frequency_second.keys():
        if '\n' in key or key == '':
            del frequency[key]
    return frequency

    
def filter_stop_words(frequency, stop_words):    
    if frequency is None or stop_words is None:
        return frequency
    frequency_copy = frequency.copy()
    frequencies = frequency.copy()
    for key in frequency_copy:
        if str(key).isdigit() or key in stop_words:
            del frequencies[key]
            continue
    return frequencies


def get_top_n(frequencies, top_n):    
    if top_n < 0:
        return ()   
    x = top_n
    top = []
    frequencies_list = []
    for key, value in frequencies.items():
        frequencies_list.append([key, value])  
    frequencies_list = sorted(frequencies_list, reverse=True)    
    for i in frequencies_list:
        if x == 0:
            break
        top.append(i[0])
        x -= 1  
    top = tuple(top)
    return top


def write_to_file(path_report, top):    
    file = open(path_report, 'w')    
    for i in top:
        file.write(i)
        file.write('\n')
    file.close()
