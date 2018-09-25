
def calculate_frequences(text):
    if text is None or str(text).isdigit() or text == "":
        return {}
    mess = '''!@/#$%^~,&*'.()_+`=-0987654321"';:'''
    frequency = {}
    text = text.lower()

    for i in text:
        if i in mess:
            text = text.replace(i, '')
    text = text.split()
    for i in text:
        num = text.count(i)
        frequency[i] = num
    return frequency


def filter_stop_words(frequency2, stop_words):
    if frequency2 is None or stop_words is None:
        return frequency2
    for i in list(frequency2):
        if str(i).isdigit():
            frequency2.pop(i)
        if i in stop_words:
            frequency2.pop(i)
    return frequency2


def get_top_n(frequencies, top_n):
    if top_n < 0:
        return()
    new = []
    dic1 = []
    for key,value in frequencies.items():
        new.append([value, key])
        continue
    sorted(new, reverse=True)
    counter = 0
    for element in new:
        if counter == top_n:
            break
        dic1.append(element[1])
        counter += 1
    res = tuple(dic1)
    return res







