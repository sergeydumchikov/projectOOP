goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_prod in goods:
    price = 0
    num_prod = 0
    product = goods[i_prod]
    for i_val in store[product]:
        price += i_val['quantity'] * i_val['price']
        num_prod += i_val['quantity']
    print(i_prod, '- {} шт, стоимость {} руб'.format(num_prod, price))