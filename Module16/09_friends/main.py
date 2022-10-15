N = int(input('Введите количество друзей: '))
K = int(input('Количество долговых расписок: '))
balance = []
nested_list = []
list = list(range(1, N + 1))

for i in list:
    nested_list.append(i)
    nested_list.append(0)
    balance.append(nested_list)
    nested_list = []

for i in range(K):
    print(i + 1, "расписка")
    whom = int(input('Кому? '))
    from_whom = int(input('От кого? '))
    how_many = int(input('Сколько? '))
    print()
    for n in balance:
        if whom == n[0]:
            n[1] = n[1] - how_many
        elif from_whom == n[0]:
            n[1] = n[1] + how_many


for i in balance:
    print(i[0], ':', i[1])