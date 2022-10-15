class_1 = list(range(160, 176 + 1, 2))
class_2 = list(range(162, 180 + 1, 3))

class_1.extend(class_2)

limit = len(class_1)
for i in range(limit):
    for n in range(i, limit):
        if class_1[n] < class_1[i]:
            class_1[n], class_1[i] = class_1[i], class_1[n]


print('Отсортированный список: ', class_1)