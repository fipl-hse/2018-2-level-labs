our_file = open('data.txt', 'r')
text = our_file.read()
our_file.close()
stop_words = input('Input stop words: \n')
top_n = int(input('How many top used words you want to see: \n'))


def count_frequency(text):
    text = text.lower()

    for i in text:
        if '\n' in i:
            text = text.replace('n', ' ')

    punctuation = [',', '<', '>', '.', '/', '"', '?', ':', ';', '}', '{',
                   '[', ']', '!', '@', '(', '#', '$', '%', '^', '&', '*',
                   '+', '-', '|', '№', '~', '`', '–', '_', '—', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in text:
        if i in punctuation or i in numbers:
            text = text.replace(i, '')

    text_list = text.split(' ')

    frequency = dict()
    for word in text_list:
        if word not in frequency:
            frequency[word] = 1
        else:
            number = frequency.get(word)
            frequency[word] = number + 1

    frequency_ws = frequency.copy()
    for key in frequency_ws.keys():
        if key == '':
            del frequency[key]

    return frequency
    filter_stop_words(frequency, stop_words)


def filter_stop_words(frequency, stop_words):
    stop_words = stop_words.lower()
    stop_words_list = stop_words.split(', ')
    stop_words_tuple = tuple(stop_words_list)

    new_frequency = frequency.copy()
    for i in new_frequency:
        for n in stop_words_tuple:
            if i == n:
                del frequency[i]

    return frequency
    get_top_n(frequency, top_n)


def get_top_n(frequency, top_n):
    frequency_list = list(frequency.items())
    frequency_sort = sorted(frequency_list, key=lambda x: x[1], reverse=True)

    result = []
    i = 0
    for element in frequency_sort:
        if i == top_n:
            break
        else:
            result.append(element[0])
            i += 1

    result = tuple(result)
    print(result)


count_frequency(text)
