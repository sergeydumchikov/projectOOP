shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

def get_price(sublist):
    for elem in sublist:
        if isinstance(elem, int):
            return elem




detail = str(input('Введите название детали: '))

count = 0
cost = 0


for pair in shop:
    if detail in pair:
        cost += get_price(pair)
        count += 1



print('Количество деталей: ', count)
print('Общая стоимость: ', cost)