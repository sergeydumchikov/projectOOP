guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    guest = str(input('Гость пришел или ушел? '))
    if guest == 'Пора спать':
        break
    name_guest = str(input('Имя гостя: '))
    if guest == 'пришел':

        if len(guests) == 6:
            print('Прости,', name_guest, 'но мест нет')
        else:
            guests.append(name_guest)
            print('Привет', name_guest)

    elif guest == 'ушел':
        if name_guest in guests:
            guests.remove(name_guest)
            print('Пока', name_guest)
        else:
            print('Такого гостя нет в списке')
    else:
        print('Ошибка ввода')

    print()
print('\nВечеринка закончилась, все легли спать')