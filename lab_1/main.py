"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    frequencies = {}

    if text == None or type(text) != str:
        return frequencies
    elif not text:
        return frequencies
    elif type(text) == str:
        for spam in text:
            if spam in """1234567890-_+=()"*&?^:%$;№'#"@3!`~:<>/\|].,}[{""":
                text = text.replace(spam, ' ')
                
        split_text = text.lower()            
        split_text = split_text.split(' ')
        
        if '\n' in split_text or '' in split_text or '\n\n' in split_text:
            while '\n\n' in split_text:
                split_text.remove('\n\n')
            while '\n' in split_text:
                split_text.remove('\n')
            while '' in split_text:
                split_text.remove('')
               
        for word in split_text:
            quantity_words = split_text.count(word)
            frequencies[word] = quantity_words

        return frequencies
    else:
        return frequencies



def filter_stop_words(freq_dict: dict, stop_words: tuple) -> dict:

    if stop_words == None or freq_dict == None:
        return None
   
    if stop_words:
        new_frequencies = freq_dict.copy()
        
        for key in freq_dict.keys():
            if key != str(key):
                new_frequencies.pop(key)
                
        for s_w in stop_words:
            if s_w in new_frequencies:
                new_frequencies.pop(s_w)
                
        return new_frequencies
    else:
        return freq_dict


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    if not top_n > 0:
        return ()
    else:
        top_n_dictionary = sorted(frequencies, key=frequencies.__getitem__, reverse=True)
        top_n_dictionary = tuple(top_n_dictionary[:top_n])
        return top_n_dictionary

