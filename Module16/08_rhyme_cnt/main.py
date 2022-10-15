number_peoples = int(input('Количество людей: '))
number = int(input('Какое число в считалке: '))
list = list(range(1, number_peoples + 1))
out = 0

for i in range(number_peoples - 1):
    print('Текущий круг людей: ', list)
    start = out % len(list)
    out = (start + number - 1) % len(list)
    print('Начало отчета с номера: ', list[start])
    print('Выбывает человек под номером: ', list[out])
    list.remove(list[out])
    print()

print('Остался человек под номером: ', list[0])



