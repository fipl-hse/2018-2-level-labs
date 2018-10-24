"""
Labour work #2
 Check spelling of words in the given  text
"""
import sys
import operator
import re
from lab_1.main import calculate_frequences
sys.path.append("2018-level-labs.lab_1 r")
REFERENCE_TEXT = ''
TEXT = ''
if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
FREQUENCIES = calculate_frequences(REFERENCE_TEXT)
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
AS_IS_WORDS = ()


def propose_candidates(word: str, max_depth_permutations: int = 3) -> str:
    cnds = set()
    mutables = set()
    if max_depth_permutations is None or not isinstance(max_depth_permutations, int) or max_depth_permutations <= 0:
        return []
    if max_depth_permutations > 1:
        for i in range(max_depth_permutations):
            if word is None or not isinstance(word, str) or word == '':
                return []
            if isinstance(word, str) and word != '':
                for d in LETTERS:
                    for ch_r in range(len(word) + 1):
                        if word[ch_r - 1].isupper():
                            cnds.add(word[:ch_r] + d.upper() + word[ch_r:])
                            mut = (word[:ch_r] + d.upper() + word[ch_r:])
                        cnds.add(word[:ch_r] + d + word[ch_r:])
                        mut = (word[:ch_r] + d + word[ch_r:])
                    for ch_r in range(len(mut) + 1):
                        if mut[ch_r - 1].isupper():
                            mutables.add((mut[:ch_r] + d.upper() + mut[ch_r:]))
                        mutables.add((mut[:ch_r] + d + mut[ch_r:]))
                for ch_r in range(len(word) - 1):
                    var = list()
                    for chars in word:
                        var.append(chars)
                    var.insert(ch_r, var[ch_r + 1])
                    var.pop(ch_r + 2)
                    cnds.add(''.join(var))
                    mut = (''.join(var))
                for ch_r in range(len(mut) - 1):
                    var1 = list()
                    for i in mut:
                        var1.append(i)
                    var1.insert(ch_r, var1[ch_r + 1])
                    var1.pop(ch_r + 2)
                    mutables.add(''.join(var1))
                for c in LETTERS:
                    for ch_r in word:
                        if ch_r.isupper():
                            cnds.add(word.replace(ch_r, c.upper(), 1))
                        cnds.add(word.replace(ch_r, c, 1))
                        mut = word
                    for ch_r in mut:
                        if ch_r.isupper():
                            mutables.add(mut.replace(ch_r, c.upper(), 1))
                        mutables.add(mut.replace(ch_r, c, 1))
                for ch_r in word:
                    cnds.add(word.replace(ch_r, '', 1))
                    mut = word
                    mutables.add(mut.replace(ch_r, '', 1))
                candidates = tuple(cnds)
                return candidates
            return None


def keep_known(candidates: tuple, frequencies: dict) -> list:
    known_freq = frequencies
    if known_freq is None:
        return []
    if candidates is None:
        return []
    if not isinstance(candidates, tuple):
        return []
    kn_w = set()
    for i in candidates:
        if i in known_freq:
            kn_w.add(i)
    new_candidates = list(kn_w)
    return new_candidates


def choose_best(frequencies: dict, candidates: tuple) -> str:
    if not frequencies:
        return 'UNK'
    adv_frequencies = frequencies.copy()
    if not candidates or tuple([]):
        return 'UNK'
    out_best = dict()
    best = []
    for k in frequencies.keys():
        if not isinstance(k, str):
            adv_frequencies.pop(k)
    for words in candidates:
        if words in adv_frequencies:
            out_best.update({words : int(adv_frequencies[words])})
        else:
            pass
    al_eq = max(out_best.items(), key=operator.itemgetter(1))[0]
    for k, value in out_best.items():
        if value >= out_best.get(al_eq):
            best.append(k)
    word = sorted(best)[0]
    return word


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word is None:
        return 'UNK'
    if as_is_words is None:
        as_is_words = tuple()
    if frequencies is None:
        return 'UNK'
    new_t = []
    for words in list(as_is_words):
        new_t.append(str(words))
    as_is_words_new = tuple(new_t)
    for exc in as_is_words_new:
        if exc.lower() == word.lower():
            word = exc.lower()
            return word
        if exc == word:
            word = exc
            return word

    if word in frequencies:
        return word
    candidates = propose_candidates(word)
    filtered_candidates = tuple(keep_known(tuple(candidates), frequencies))
    word = choose_best(frequencies, filtered_candidates)
    return word


def spell_check_text(frequencies: dict, as_is_words: tuple, text: str):
    freq_dict = frequencies
    check_text = text
    w_out = re.findall(r"[\w']+|[.,!?;]", check_text)
    for word in w_out:
        if word in as_is_words:
            pass
        if word.isalnum():
            w_out[w_out.index(word)] = spell_check_word(freq_dict, as_is_words, word)
        else:
            pass
    w_out = re.sub(r'\s([?.!"](?:\s|$))', r'\1', ' '.join(w_out))
    return w_out
