#Laboratory work 1

alph = '" "abcdefghijklmnopqrstuvwxyz'
d_freq = {}
stop_words = ('the', 'over', 'here', 'that', 'on', 'up', 'down', 'a')
dict_3 = {}
top_n = int(input('Сколько первых по популярности слов вывести? Укажите число: '))

def calculate_frequences(text:str):
  text = str(text)
  text = text.lower()
  for e in text:
    if e not in alph:
      text = text.replace(e,"")
  text = text.split(' ')
  for e in text:
    if e not in d_freq:
      d_freq[e] = 1
    else:
      d_freq[e] += 1
  return d_freq

func1 = calculate_frequences(text)
print ('Результат I функции: ', func1)


def filter_stop_words(d_freq, stop_words):
  d_freq_copy = d_freq.copy()
  for e in stop_words:
    if e in d_freq_copy.keys():
      d_freq_copy.pop(e)
  return d_freq_copy
d_freq_filt = filter_stop_words(d_freq, stop_words)

func2 = filter_stop_words(d_freq, stop_words)
print ('Результат II функции: ', func2)

def get_top_n(d_freq_filt, top_n):
  l_intr = []
  for key, value in d_freq_filt.items():
    l_intr.append([value, key])
  l_intr.sort(reverse = True)
  test = 0
  top_n_list = []
  for e in l_intr:
    if test == top_n:
      break
    top_n_list.append(e[1])
    test += 1
  top_n_list = tuple(top_n_list)
  return top_n_list

func3 = get_top_n(d_freq_filt, top_n)
print ('Результат III функции: ', func3)