text = "The quick brown fox jumps over the lazy dog"
stop_words = ("the", "over")


def calculate_frequences(text):
    work_words = []
    frequencies = {}
    if not text:
        return {}
    if type(text) != str:
        return {}

    if type(text) == str:
        ready_text = text.lower()
        words = ready_text.split(' ')

        if '\n' in words:
            while '\n' in words:
                words.remove('\n')
        if '' in words:
            while '' in words:
                words.remove('')

        for index, word in enumerate(words):
            cleanword = ''
            if not word.isalpha():
                for i in word:
                    if i.isalpha():
                        cleanword += i
                if cleanword:
                    work_words.append(cleanword)
            else:
                work_words.append(cleanword)

        for word in work_words:
            num_words = work_words.count(word)
            frequencies[word] = num_words

    return frequencies


def filter_stop_words(frequencies, stop_words):

    if not frequencies:
        return frequencies

    dictionary1 = frequencies.copy()

    for key in frequencies.keys():
        if type(key) != str:
            dictionary1.pop(key)
        if stop_words:
            for word_stop in stop_words:
                if word_stop in dictionary1:
                    dictionary1.pop(word_stop)
                else:
                    pass

    return dictionary1


def get_top_n(frequencies, top_n):

    res = []
    l = list(frequencies.values())
    l.sort()
    l.reverse()
    for i in range(len(l) - top_n):
        l.pop()

    for list_el in l:
        for key, value in frequencies.items():
            if value == list_el:
                res.append(key)
                del frequencies[key]
                break

    res = tuple(res)
    return res
