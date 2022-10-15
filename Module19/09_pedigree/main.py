N = int(input('Введите кол-во человек: '))
tree_dict = dict()
parent_dict = dict()

for pair in range(N - 1):
    print(pair+1, 'пара: ', end='')
    child, parent = input().split()
    tree_dict[child] = parent
    parent_dict[child] = 0
    parent_dict[parent] = 0

for i in tree_dict:
    s = i
    while s in tree_dict:
        s = tree_dict[s]
        parent_dict[i] += 1

print('“Высота” каждого члена семьи:')
for i in sorted(parent_dict):
    print(i, parent_dict[i])
