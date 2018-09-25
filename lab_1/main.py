"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
def read_from_file(path_to_file: str, lines_limit: int) -> str:
    file = open(path_to_file, 'r')
    file = file.read()
    text_to_work = ''
    i = 0
    for line in file:
        if i == lines_limit:
            break   
        else:
            #line_imp = line + '\n'
            text_to_work += line + '\n'
            i += 1
            continue
    return text_to_work 


def calculate_frequences(text: str) -> dict:
    if text != None and type(text) != int:
        frequencies = {}
        new_text = text.lower()
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        clean_text = ''
        if ' ' not in text:
             clean_list = text.split(None)
             frequencies = {token: clean_list.count(token) for token in clean_list}
             return frequencies
        else:
             i = 0
             for i in range(len(new_text)):
                 if new_text[i] not in alphabet:
                     clean_text = new_text.replace(text[i], ' ')
                     new_text = clean_text
             clean_list = []
             clean_list = clean_text.split(' ')
             frequencies = {token: clean_list.count(token) for token in clean_list}
             if '' in frequencies:
                 frequencies.pop('')
             return frequencies
    else:
        frequencies = {}
        return frequencies

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    new_frequencies = {}
    if stop_words ==  None or frequencies == None:
        return new_frequencies
    else:
        for key in frequencies.keys():
            if type(key) != str:
                del frequencies[key]
                return frequencies
        for word in frequencies.keys():
            if word not in stop_words:
                new_frequencies[word] = frequencies.get(word)
        return new_frequencies

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    list_keys = []
    if top_n <= 0:
        tuple_top = ()
        return tuple_top
    else:
        for key in frequencies.keys():
            list_keys.append(key)
        slice_keys = list_keys[: top_n]
        tuple_top = tuple(slice_keys)
        return tuple_top
    
    
def write_to_file(path_to_file: str, content: tuple):
    report = open(path_to_file, 'w')
    for token in content:
        #inside = token + '\n'
        report.write(token + '\n')
        continue
    report.close() 
    return True
