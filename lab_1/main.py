mat = input('''Введите текст, который нужно обработать или имя файла, который нужно открыть (с форматом)''')
if mat[-4:0] == ".txt":
    f = open(mat,'r')
    text = f.read()
else:
    text = mat
def calculate_frequences(text) -> dict:
    prom1 = text.split()
    punct_marks = ''':;!(){}[]"',?/.<>\n'''
    for i in range(0, len(prom1)):
        for c in prom1[i]:
            if c in punct_marks and c in prom1[i]:
                prom1[i] = prom1[i].replace(c, "")
    frequency = {}
    for i in range(0, len(prom1)):
        prom1[i] = prom1[i].lower()
        frequency[prom1[i]] = prom1.count(prom1[i])
        if prom1[i] in prom1[i - 1::-1]:
            continue
    return frequency
freq_dict = calculate_frequences(text)
stop_words = ["на","и","в","я","не","ты","мне","с","до","как","от","но","о"]
def filter_stop_words(freq_dict, stop_words) -> dict:
    freq_dict = {k: freq_dict[k] for k in freq_dict if k not in stop_words}
    return freq_dict
new_freq_dict = filter_stop_words(freq_dict, stop_words)
n = int(input("Введите желаемое число самых популярных слов"))
def get_top_n() -> tuple:
    slova = []
    chastoty = []
    for k, v in freq_dict.items():
        slova.append(k)
        chastoty.append(v)
        final_top = []
    if n <= len(slova):
        while len(final_top) != n:
            maxi = max(chastoty)
            for k in freq_dict.keys():
                if freq_dict[k] == maxi:
                    final_top.append(k)
                    chastoty.remove(maxi)
    else:
        n = len(slova)
        while len(final_top) != n:
            maxi = max(chastoty)
            for k in freq_dict.keys():
                if freq_dict[k] == maxi:
                    final_top.append(k)
                    chastoty.remove(maxi)
    final_top = tuple(final_top)
    return final_top
final = top_n(freq_dict, n)
