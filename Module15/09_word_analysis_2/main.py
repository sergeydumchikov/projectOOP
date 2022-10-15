word = str(input('Введите слово: '))
word_list = list(word)
reverse_list = []

for i in range(len(word_list) - 1, -1, -1):
    reverse_list.append(word_list[i])

if word_list == reverse_list:
    print('Слово', word, 'является палинромом')
else:
    print('Слово', word, 'не является палинромом')