def read_from_file():
    with open(r'C:\Users\admin\Downloads\2018-2-level-labs\Beatles - Yesterday.txt') as f:
        t = f.read()
        return t


text = read_from_file()


def calculate_frequences(text):
    if text == '':
        return {}
    elif type(text) != str:
        return {}
    else:
        text = text.lower()
        prom1 = text.split()
        punct_marks = '''@#$%^&*()+-~1234567890:;!(){}[]"',?/.<>\n'''
        for i in range(0, len(prom1)):
            for c in prom1[i]:
                if c in punct_marks and c in prom1[i]:
                    prom1[i] = prom1[i].replace(c, "")
        for i in range(0, len(prom1)):
            for c in prom1:
                if c == '':
                    prom1.remove(c)
        frequency = {}
        for i in range(0, len(prom1)):
            frequency[prom1[i]] = prom1.count(prom1[i])
            if prom1[i] in prom1[i - 1::-1]:
                continue
    return frequency
res = calculate_frequences(text)
stop_words = ["i", "do", "an", "not", "to", "on", "the"]
def filter_stop_words(res, stop_words):
    if res == None or stop_words == None:
        return None
    res = {k: res[k] for k in res if k not in stop_words and type(k) == str}
    return res
filtered_dict = filter_stop_words(res, stop_words)
n = 5
def get_top_n(filtered_dict, n):
    final_top = ()
    list_res = []
    if filtered_dict == {}:
        return ()
    elif filtered_dict == None or n == None or type(n) != int:
        return None
    else:
        if n >= len(filtered_dict):
           final_top = tuple(filtered_dict.keys())
        else:
           slova = []
           chastoty = []
           for k,v in filtered_dict.items():
               slova.append(k)
               chastoty.append(v)
           while len(list_res) < n:
                 maxi = max(chastoty)
                 for c in slova:
                     if filtered_dict[c] == maxi:
                        list_res.append(c)
                        slova.remove(c)
                 chastoty.remove(maxi)
                 if len(list_res)> n:
                    list_res = list_res[0:n]
                    break
           final_top = tuple(list_res)
        return final_top
final = get_top_n(filtered_dict, n)
def write_into_file():
    with open('report.txt', 'w') as op:
        op.write("Результат работы функции calculate_frequences" + "\n")
        for k, v in res.items():
            op.write(k + ":" + str(v))
            op.write("\n")
        op.write("Результат работы функции filter_stop_words" + "\n")
        for k, v in filtered_dict.items():
            op.write(k + ":" + str(v))
            op.write("\n")
        op.write("Результат работы функции get_top_n" + '\n')
        for c in final:
            op.write(c + ";" + " ")
    with open("report.txt", "r") as re:
        m = re.read()
        return m
chit = write_into_file()
print(chit)
