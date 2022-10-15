number_nvida = int(input('Количество видеокарт: '))
nvida_list = []
new_nvida_list = []
for i in range(1, number_nvida + 1):
    print(i, 'видеокарта: ', end='')
    new_card = int(input())
    nvida_list.append(new_card)

print('Старый список видеокарт: ', nvida_list)

for i in range(0, number_nvida ):
    if nvida_list[i] != max(nvida_list):
        new_nvida_list.append(nvida_list[i])

print('Новый список видеокарт: ', new_nvida_list)


