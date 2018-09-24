f = open('data.txt', 'r')
text = f.read()
f.close()


def calculate_frequences(text) -> dict:
    punctuation = [',', '.', '<', '>', '/', '?', ';', ':', '*', '`', '~', '!',
                   '#', '$', '%', '^', '(', ')',
                   '-', '_', '@', '+', '=', '{', '[', '}', ']', '|']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in text:
        if '\n' in i:
            text = text.replace('\n', ' ')
    for i in text:
        if i in punctuation or i in numbers:
            text = text.replace(i, '')
    text_l = text.lower()
    text_split = text_l.split(' ')
    frequency = {}
    for i in text_split:
        if i not in frequency:
            frequency[i] = 1
        else:
            num = frequency.get(i)
            frequency[i] = num+1
    if '' in frequency:
        del frequency['']
    return frequency
    stop_words = input('Please, input the stop words ')
    top_n = int(input('Please, input how many top used words you want to see '))
    filter_stop_words(frequency, stop_words)
    get_top_n(frequency, top_n)
    pass


def filter_stop_words(frequency, stop_words) -> dict:
    stop_words = stop_words.lower()
    stop_words = stop_words.split(', ')
    frequency_clean = frequency.copy()
    frequency_copy = frequency.copy()
    for i in frequency_copy:
        for n in stop_words:
            if i == n:
                del frequency_clean[i]
    return frequency_clean
    pass


def get_top_n() -> tuple:
    freq_list = list(frequency.items())
    freq_sort = sorted(freq_list, key=lambda x: x[1], reverse=True)
    count = 0
    top = []
    for i in freq_sort:
        if count == top_n:
            break
        else:
            top.append(i[0])
            count += 1
    top = tuple(top)
    file = open('report.txt', 'w')
    for i in top:
        file.write(i)
        file.write('\n')
    file.close()
    pass
