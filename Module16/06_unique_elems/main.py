first_list = []
second_list = [2, 4, 6, 3, 3, 2, 1]

for i in range(3):
    print('Введите', i + 1, 'элемент списка: ', end='')
    element = int(input())
    first_list.append(element)

first_list.extend(second_list)

for elem in first_list:
    while first_list.count(elem) != 1:
        first_list.remove(elem)

print(first_list)