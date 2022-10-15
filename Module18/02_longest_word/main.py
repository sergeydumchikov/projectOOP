strin = input('Введите строку: ').split()
max_word = ''
for i_word in strin:
    if len(str(i_word)) > len(str(max_word)):
        max_word = i_word

print('Самое длинное слово: ', max_word)
print('Длина этого слова: ', len(str(max_word)))
