
string = input('Введите строку: ')
count = 0
shifr = ''
for i in range(len(string)):
    count += 1
    if i == len(string) - 1:
        shifr += ''.join([string[i] + str(count)])
        break
    if string[i] != string[i+1]:
        shifr += ''.join([string[i] + str(count)])
        count = 0
print('Закодированная строка:', shifr)