word = str(input('Введите слово: '))
word_list = list(word)
unic_letter = 0
for i in range(len(word_list)):
    count = 0
    for n in range(len(word_list)):
        if word_list[n] == word_list[i]:
            count += 1


    if count < 2:
        unic_letter += 1

print('Количество уникальных букв: ', unic_letter)




