test = open(r'C:\Users\Andrew\Desktop\2018-2-level-labs\test_file.txt')
test_text = ''
count = 0
limit = 5
for line in test:
    if count == limit:
        break
    print(line)
    test_text += line
    count += 1
print(test_text)
