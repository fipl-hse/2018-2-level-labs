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
stop_words = ["i", "do", "an", "not", "to","on","the"]
def filter_stop_words(res, stop_words):
    if res == None or stop_words == None:
       return None
    res = {k: res[k] for k in res if k not in stop_words}
    return res
filtered_dict = filter_stop_words(res, stop_words)
n = int(input("Введите число"))
def get_top_n(filtered_dict, n):
    if filtered_dict == {}:
       return()
    elif filtered_dict == None or n == None:
       return None
    slova = []
    chastoty = []
    smax = []
    for k,v in filtered_dict.items():
        slova.append(k)
        chastoty.append(v)
    while True:
          maxi = chastoty[0]
          for i in range(1,len(chastoty)):
              if chastoty[i] > maxi:
                 maxi = chastoty[i]
          for c in slova:
              if filtered_dict[c] == maxi:
                 smax.append(c)
                 slova.remove(c)
          chastoty.remove(maxi)
          chastoty = chastoty[:]
          if len(smax) < n:
             continue
          elif len(smax) == n:
             final_top = smax
             break
          elif len(smax) > n:
             final_top = smax[0:n]
             break
    final_top = tuple(final_top)
    return final_top
final = get_top_n(filtered_dict, n)
def write_into_file():
    with open('report.txt','w') as op:
         op.write("Результат работы функции calculate_frequences"+"\n")
         for k,v in res.items():
             op.write(k + ":" + str(v))
             op.write("\n")
         op.write("Результат работы функции filter_stop_words"+"\n")
         for k,v in filtered_dict.items():
             op.write(k + ":" + str(v))
             op.write("\n")
         op.write("Результат работы функции get_top_n"+'\n')
         for c in final:
             op.write(c + ";" + " ")
    with open("report.txt","r") as re:
         m = re.read()
         return m
chit = write_into_file()
print(chit)