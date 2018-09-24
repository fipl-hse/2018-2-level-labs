"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""

# 0: входные данные
text = input('enter your text: \n')
text = text.lower()
text = text.split(' ')  # теперь это список из слов в тексте (с повторами)
stopwords = ("actually", "like", "the", "at", "or", "sunday", "place")
print(text)

# 1: функция, создающая частотный словарь

def calculate_frequences(text):

    for word in text:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    return freq_dict

# 2: очистка словаря от стоп-слов

def filter_stop_words(freq_dict_clean, stopwords):

    print(freq_dict_clean)

    for key in list(freq_dict_clean):
        if key in stopwords:
            del freq_dict_clean[key]
    print(freq_dict_clean) ### del

    return freq_dict_clean

# 3: выстраивание топ-n  самых частых слов

def get_top_n(freq_dict_clean, top_n):

    #top_n = int(input('enter n for top_n: \n'))

    for k, v in freq_dict_clean.items():  # здесь нужно пройти по парам ключ-значение в словаре и накопить их в список (вложенные списки)
        freq_list.append([v,k])
    print(freq_list)
    freq_list.sort(reverse=True)
    print(freq_list) ### del

    top_freq_list = freq_list[:top_n]
    print(top_freq_list) ### del

    final_top_freq_list = []
    for i, element in enumerate(top_freq_list):
        final_top_freq_list.append(element[1])

    final_top_freq_list = tuple(final_top_freq_list)
    print(final_top_freq_list) ### del

    return final_top_freq_list

    # добавить защиту, если текст некорректен/пуст
    # добавить чтение из файла

freq_dict = {}
freq_list = []
