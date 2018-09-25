
def calculate_frequences(text):
    if text == None or str(text).isdigit() or text == "":
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


def filter_stop_words(frequency2,stop_words):
    if frequency2 == None or stop_words == None:
        return frequency2
    for i in list(frequency2):
        if str(i).isdigit():
            frequency2.pop(i)
        if i in stop_words:
            frequency2.pop(i)
    return frequency2


def get_top_n(frequencies, top_n):
    #new = []
    #for key,value in frequencies.items():
        #new.append([value, key])
    #sorted(new.items(), key=lambda i: i[1], reverse=True)
    #sorted(new, reverse=True)
    #dic1 = []
    #counter = 0
    #for element in new:
        #if counter == top_n:
            #break
        #dic1 = dic1.append(element[1])
        #counter += 1
    #res = tuple(dic1)
    #return res
    res = []
    counter = 0

    for key in frequencies.keys():
        if counter == top_n:
            break
        res.append(key)
        counter +=1
    return tuple(res)








# f = calculate_frequences(text)
# frequency2 = f.copy()
# print('calculate_frequencies',f)
# b = filter_stop_words(frequency2,stop_words)
# print('filter_stop_words',b)
# c =  tuple(get_top_n (b,top_n))
# print('get_top_n', c)
