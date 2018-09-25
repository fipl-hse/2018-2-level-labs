
def calculate_frequences(text: str) -> dict:
    frequences = {}
    if type(text) == str:
        for i in text:
            if i.isalpha():
                pass
            else:
                text = text.replace(i, ' ')
        text = text.lower()
        words = text.split(' ')
        for w in words:
            if w.isalpha():
                if w in frequencies.keys():
                    k = frequencies[w]
                    frequencies[w] = k + 1
                else:
                    frequencies[w] = 1

        return frequencies
    elif text == None or type(text) != str:
        return frequencies
    
def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    frequencies1 = {}
    for i in frequencies.keys():
        if type(i) == str:
            if type(stop_words) == tuple:
                dct1 = dict(frequencies)
                for k, v in dct1.items():
                    if k in stop_words:
                        del frequencies[k]
                return frequencies
            elif stop_words != tuple:
                return frequencies1
        else:
            return frequencies1
   
    
    
def get_top_n(frequencies: dict, top_n: int) -> tuple:
    tup1 = ()
    if type(frequencies) == dict and type(top_n) == int and top_n > 0:
        res = []
        l = list(frequencies.values())
        l.sort()
        l.reverse()
        for i in range(len(l) - top_n):
            l.pop()

        for list_el in l:
            for k, v in frequencies.items():
                if v == list_el:
                    res.append(k)
                    del frequencies[k]
                    break

        res = tuple(res)
        print(res)
        return res
    else:
        print(tup1)
        return tup1
  
   



