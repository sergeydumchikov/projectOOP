number = int(input('Введите размер списка: '))
print([x % 5 if x % 2 else 1 for x in range(number)])