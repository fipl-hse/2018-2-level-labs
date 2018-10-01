
def calculate_frequences(info):
    wrongs = "1234567890~@#$%^&*\"[]{}\'/\n:;!?().,<>"
    frequencies_dictionary = {}
    if type(info) is str:
        text = info.lower()
        for i in wrongs:
            text = text.replace(i, "")
        words = text.split()
        for count, k in enumerate(words):
            if words[count] in frequencies_dictionary:
                frequencies_dictionary[words[count]] += 1
            else:
                frequencies_dictionary[words[count]] = 1
    return frequencies_dictionary


def filter_stop_words(freq_dict, stopwords):
    frequencies = {}
    if not stopwords:
        stopwords = []
    if freq_dict:
        frequencies = {key: freq_dict[key] for key in freq_dict if (key not in stopwords) and (type(key) is str)}
    return frequencies


def get_top_n(sorted_words, top_n):
    words = sorted(sorted_words.items(), key=lambda item: item[1], reverse=True)
    if top_n > len(words):
        top_n = len(words)
    output = tuple(words[i][0] for i in range(top_n))
    return output


def read_from_file(path_to_file, lines_limit):
    text = open(path_to_file)
    info = text.read(lines_limit)
    return info


def write_to_file(path_to_file, content):
    text = open(path_to_file, "w")
    text.write(content)
    text.close()
