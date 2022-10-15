import random

N = 10
K = 3

list_throw = ['I' for _ in range(1, 11)]
for throw in range(1, K + 1):
    L_i = random.randint(1, 10)
    R_i = random.randint(1, 10)
    if L_i > R_i:
        L_i, R_i = R_i, L_i
    print('Бросок', throw, '. Сбиты палки с номера', L_i + 1, 'по номер', R_i)

    list_throw[L_i:R_i] = '.' * len(list_throw[L_i :R_i])

print('Результат:', list_throw)