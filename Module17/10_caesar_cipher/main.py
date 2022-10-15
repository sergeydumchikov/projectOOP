def shifr(string, step):
    char_list = [(alph[(alph.index(sym) + step) % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
inp = input('Введите строку: ')
shift = int(input('Введите сдвиг: '))

out = shifr(inp, shift)

print('Зашифрованная строка: ', out)