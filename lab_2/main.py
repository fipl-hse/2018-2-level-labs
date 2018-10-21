"""
Labour work #2
 Check spelling of words in the given  text
"""
#from lab_1.main import calculate_frequences

#LETTERS = 'abcdefghijklmnopqrstuvwxyz'
#REFERENCE_TEXT = ''

#if __name__ == '__main__':
    #with open('very_big_reference_text.txt', 'r') as f:
        #REFERENCE_TEXT = f.read()
        #freq_dict = calculate_frequences(REFERENCE_TEXT)
alphabet = "abcdefghijklmnopqrstuvwxyz"
lst = []
lst1 = []
lst2 = []
word = "dog"
for j in range(0, len(alphabet)):
    for i in range(0,len(word)):
        word = list(word)
        word.insert(i, " ")
        lst.append(word)
        for i in range(0,len(lst)):
            lst[i] = ''.join(lst[i])
            lst[i] = lst[i].replace(" ", alphabet[j])
print(lst)
