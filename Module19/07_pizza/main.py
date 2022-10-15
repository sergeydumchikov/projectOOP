def order_func(name, pizza, numbers):
    if name in order:
        if pizza in order[name]:
            order[name][pizza] += int(numbers)
        else:
            order[name][pizza] = int(numbers)
    else:
        values_name[pizza] = int(numbers)
        order[name] = values_name
    return order

num_ord = int(input('Введите кол-во заказов: '))
order = dict()
values_name = dict()

for i_ord in range(num_ord):
    print(i_ord+1, 'заказ: ', end='')
    inp_data = input().split()
    order_func(inp_data[0], inp_data[1], inp_data[2])
    values_name = dict()

for key in sorted(order.keys()):
    print(key, ':')
    for key_n in sorted(order[key].keys()):
        print(' '* 5, key_n, ':', order[key][key_n])