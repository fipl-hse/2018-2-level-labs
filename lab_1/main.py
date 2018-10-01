text = "The quick brown fox jumps over the lazy dog"
stop_words = ("the", "over")


def calculate_frequences(text):
    frequencies = {}
    if not text:
        return {}
    if type(text) != str:
        return {}

    if type(text) == str:
        ready_text = text.lower()

        not_needed = """`~!@#$%^&*()-_=+{[}]:;'",<.>/?1234567890\|"""

        for symbol in not_needed:
            ready_text = ready_text.replace(symbol, "")
            if symbol == "/n":
                ready_text = ready_text.replace(symbol, " ")

        words = ready_text.split()

        for i in range(0, len(words)):
            frequencies[words[i]] = words.count(words[i])

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
    if frequencies == {} or top_n <= 0:
        return ()
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