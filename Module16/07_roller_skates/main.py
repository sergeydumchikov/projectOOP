
skates = []
foot_size = []
number_skate = int(input('Введите количество коньков: '))

for i_sk in range(number_skate):
    print('Размер', i_sk + 1, ' пары: ', end='')
    skate = int(input())
    skates.append(skate)

number_peoples = int(input('Количество людей: '))
count = 0

for i_pe in range(number_peoples):
    print('Размер ноги', i_pe + 1, ' человека: ', end='')
    people = int(input())
    for i in skates:
        if i >= people:
            count += 1
            skates.remove(i)

print('Наибольшее кол-во людей, которые могут взять ролики:', count)

