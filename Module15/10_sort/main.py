old_list = [1, 4, -3, 0, 10]
print('Изначальный список: ', old_list)
limit = len(old_list)
for i in range(limit):
    for n in range(i, limit):
        if old_list[n] < old_list[i]:
            old_list[n], old_list[i] = old_list[i], old_list[n]


print('Отсортированный список: ', old_list)