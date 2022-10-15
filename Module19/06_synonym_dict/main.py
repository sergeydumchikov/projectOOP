num_words = int(input('Введите кол-во пар слов: '))
words_dict = dict()

for pair in range(num_words):
    print(pair+1, 'пара: ', end='')
    words_list = input().split(' - ')
    words_dict[words_list[0]] = words_list[1]
    words_dict[words_list[1]] = words_list[0]

while True:
    check = input('\nВведите слово: ')
    if check in words_dict.keys():
        print('Синоним:', words_dict[check])
        False
    else:
        print('Такого слова нет в словаре')
