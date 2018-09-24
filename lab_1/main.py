"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text_first: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    # Шаг 0. Уберем возможность неверного ввода.
    if text_first is None or str(text_first).isdigit():
        dictionary_freq = {}
        return dictionary_freq

    # Шаг 1. Пройдемся по тексту и уберем лишние символы.
    for element_word in text_first:
        if element_word in """1234567890_-=!@#$%^&*()~_+[]{}:;'",./><?""":
            text_first = text_first.replace(element_word, ' ')
            continue
    text_first = text_first.lower()
    text_first = text_first.split()

    # Шаг 2. Создадим словарь частотности.
    dictionary_freq = {}
    for word_first in text_first:
        frequency_word = text_first.count(word_first)
        dictionary_freq[word_first] = frequency_word
        continue

    # Шаг 4. Возвращаем полученный, отсортированный словарь частот.
    return dictionary_freq


def filter_stop_words(frequencies_dictionary: dict, stop_words_list: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    # Шаг 0. Уберем возможность неверного ввода.
    if stop_words_list is None or frequencies_dictionary is None:
        return frequencies_dictionary

    # Шаг 1. Пройдемся по словарю и исключим ненужные слова.
    for key in list(frequencies_dictionary):
        if str(key).isdigit() or key in stop_words_list:
            frequencies_dictionary.pop(key)
            continue

    # Шаг 2. Возвращаем отфильтрованный словарь.
    return frequencies_dictionary


def get_top_n(frequencies_last: dict, top_n_first: int) -> tuple:
    """
    Takes first N popular words
    """
    # Шаг 0. Уберем возможность неверного ввода.
    if top_n_first < 0:
        return ()

    # Шаг 1. Пройдемся по словарю н-раз. Запишем в список пару значение-ключ.
    check_list = []
    for key, value in frequencies_last.items():
        check_list.append([value, key])
        continue

    # Шаг 1.1. Отсортируем список с правильным порядком. От большей частоты к меньшей.
    sorted(check_list, reverse=True)

    # Шаг 2. Запишем н-слов с наибольшей частотой.
    final_res = []
    counter_check = top_n_first
    for element in check_list:
        if counter_check == 0:
            break
        final_res.append(element[1])
        counter_check -= 1
    result_final = tuple(final_res)

    # Шаг 4. Вернем результат.
    return result_final


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    # data.txt

    # Шаг 1. Прочитаем файл.
    text = open(path_to_file, 'r')
    text = text.read()

    # Шаг 2. Пройдемся по строчкам файла и запишем нужное количество строк в новую строку.
    text_new = ''
    counter = 0
    for line in text:
        if counter == lines_limit:
            break
        else:
            text_new += line + '\n'
            counter += 1
            continue

    # Шаг 3. Возвращаем записанную из файла строку.
    return text_new


def write_to_file(path_to_file: str, content: tuple):
    # report.txt

    # Шаг 1. Откроем файл для записи.
    file_new = open(path_to_file, 'w')

    # Шаг 2. Пройдемся по элементам кортежа и запишем их в файл. Каждое слово с новой строки.
    for element in content:
        file_new.write(element + '\n')
        continue

    # Шаг 3. Закроем файл.
    file_new.close()
    return True
