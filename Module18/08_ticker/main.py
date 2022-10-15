string_1 = input('Введите первую строку: ')
string_2 = input('Введите вторую строку: ')
compare = 0

if string_1 == string_2:
    print('Первая строка идентична без сдвигов')
else:
    string_1 = list(string_1)
    for i_elem in range(len(string_1)):
        string_1.insert(0, string_1[len(string_1) - 1])
        string_1 = string_1[:len(string_1) - 1:]
        if ''.join(string_1) == string_2:
            compare = 1
            print('Первая строка получается из второй со сдвигом ', i_elem + 1)
            break
    if compare == 0:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


