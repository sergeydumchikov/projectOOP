N = int(input('Введите целое число: '))
list_numbers = []
for i in range(1, N + 1):
    if i % 2 != 0:
        list_numbers.append(i)
print('Список нечетных чисел от 1 до N:\n', list_numbers)
