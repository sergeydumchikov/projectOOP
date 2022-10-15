name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
scores_list = []

numbers = len(name_list)
for i in range(2, numbers, 2):
    scores_list.append(name_list[i])
print('Список участников с четными индексами:\n', scores_list)