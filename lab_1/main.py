
def calculate_frequences(text):
    if text == None or str(text).isdigit() or text == "":
        return {}
    mess = '''!@/#$%^~,&*'.()_+`=-0987654321"';:'''
    frequency = {}
    text = text.lower()

    for i in text:
        if i in mess and i in text:
            text = text.replace(i, '')
    text = text.split()
    for i in text:
        num = frequency[i]
        frequency[i] = num + 1
    return frequency


def filter_stop_words(frequency2,stop_words):
    for i in list(frequency2):
        if i.isdigit():
            frequency2.pop(i)
        if i in stop_words:
            frequency2.pop(i)
    return frequency2


def get_top_n(frequences,top_n):
    if not top_n > 0:
        return ()
    dic = sorted(frequences.items(), key = lambda i:i[1], reverse=True)
    dic1=()
    for i in range(0,top_n):
        dic1 = dic1 + dic[i]
    if top_n == 0:
        dic1 = dic
    return dic1


print('check that')
# f = calculate_frequences(text)
# frequency2 = f.copy()
# print('calculate_frequencies',f)
# b = filter_stop_words(frequency2,stop_words)
# print('filter_stop_words',b)
# c =  tuple(get_top_n (b,top_n))
# print('get_top_n', c)
