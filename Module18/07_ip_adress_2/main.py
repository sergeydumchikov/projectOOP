
def numbers(adress):
    count = 0
    for i_sym in adress:
        if i_sym.isdigit() == False and i_sym != '':
            print(i_sym, '- не целое число')
            count = 1
            break
        elif i_sym != '' and int(i_sym) > 255:
            print(i_sym, 'превышает 255')
            count = 1
            break
    if len(adress) < 4 or adress[len(adress) - 1] == '':
        print('Адрес - это четыре числа, разделенные точками')
        count = 1
    elif count == 0:
        print('IP-адрес корректен')


adr = input('Введите IP: ').split('.')
numbers(adr)



