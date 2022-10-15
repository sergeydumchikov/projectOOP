num_town = int(input('Введите кол-во стран: '))
towns = dict()

for i_cotr in range(num_town):
    print(i_cotr + 1, end=' ')
    country = input('страна: ').split()
    towns.update(dict.fromkeys(country[1:], country[0]))

for i_tow in range(3):
    print(i_tow + 1, end=' ')
    town = input('город: ')
    if town in towns:
        print('Город', town, 'расположен в стране', towns[town])
    else:
        print('Ошибка. Такого города нет в списке')

