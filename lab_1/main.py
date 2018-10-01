#def read_from_file():
    #f = open(r'C:\Users\admin\Downloads\2018-2-level-labs\Beatles - Yesterday.txt', 'r')
    #c = f.read()
    #return c
#text = read_from_file()
text = "She'#$ %& *sells()4 %$seashells+-  45 on @@the! !!seashore#$"
def calculate_frequences(text):
    if text == '':
       return {}
    else:
       prom1 = text.split()
       punct_marks = '''+-1234567890:;!(){}[]"',?/.<>\n'''
       for i in range(0, len(prom1)):
           for c in prom1[i]:
               if c in punct_marks and c in prom1[i]:
                  prom1[i] = prom1[i].replace(c, "")
       frequency = {}
       for i in range(0, len(prom1)):
           if prom1[i] in prom1[i - 1::-1]:
            continue
    return frequency
res = calculate_frequences(text)
stop_words = ["i", "do", "an", "not", "to"]
def filter_stop_words(res, stop_words):
    res = {k: res[k] for k in res if k not in stop_words}
    return res
filtered_dict = filter_stop_words(res, stop_words)
n = 4
def get_top_n(filtered_dict, n):
    final_top = []
    slova = []
    chastoty = []
    for k,v in filtered_dict.items():
        slova.append(k)
        chastoty.append(v)
    smax = []
    while True:
          maxi = chastoty[0]
          smax = []
          for i in range(1, len(chastoty)):
              if chastoty[i] > maxi:
                 maxi = chastoty[i]
          ch = chastoty.count(maxi)
          for c in slova:
              if filtered_dict[c] == maxi:
                 smax.append(c)
                 slova.remove(c)
          chastoty.remove(maxi)
          if len(smax) > n:
             break
    final_top = smax[0:n+1]
    final_top = tuple(final_top)
    return (final_top)
final = get_top_n(filtered_dict, n)
#def write_into_file():
    #zapis = open('report.txt', 'w')
    #for k, v in res.items():
        #t = k + ":" + str(v) + "," + "\n"
        #zapis.write(t)
    #for k, v in filtered_dict.items():
        #u = k + ":" + str(v) + "," + "\n"
        #zapis.write(u)
    #for c in final:
        #v = c + "\n"
        #zapis.write(v)
    #zapis.close()
    #r = open('report.txt', 'r')
    #o = r.read()
    #return o
#m = write_into_file()
#print(m)
print(res)
print(filtered_dict)
print(final)
