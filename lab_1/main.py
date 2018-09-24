our_file = open('data.txt', 'r')
text = our_file.read()
our_file.close()
stop_words = input('Input stop words: \n')
top_n = int(input('How many top used words you want to see: \n'))

def count_frequency(text: str) -> dict:

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
    get_top_n(frequencies)


def filter_stop_words(frequency: dict, stop_words: str) -> dict:

    stop_words = stop_words.lower()
    stop_words_list = stop_words.split(' ')
    stop_words_tuple = tuple(stop_words_list)

    frequencies = frequency.copy()
    for i in frequency:
        for n in stop_words_tuple:
            if i == n:
                del frequencies[i]

    return frequencies


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    frequencies_list = list(frequencies.items())
    frequencies_sort = sorted(frequencies_list, key=lambda x: x[1], reverse=True)

    result = []
    x = 0
    for i in frequencies_sort:
        if x == top_n:
            break
        else:
            result.append(i[0])
            x += 1

    result = tuple(result)
    print(result)


count_frequency(text)
