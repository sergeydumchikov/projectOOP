
cell_number = int(input('Количество клеток: '))
cell_list = []

for i in range(1, cell_number + 1):
    print('Эффективность', i, 'клетки: ', end='')
    efficiency_cell = int(input())
    if efficiency_cell < i:
        cell_list.append(efficiency_cell)

print('Неаподходящие значения:', cell_list)


