container_list = []
number_cont = int(input('Введите количество контейнеров: '))

for i in range(number_cont):
  container_weight = int(input('введите вес контейнера: '))
  if container_weight > 200:
    print('Ошибка ввода')
  else:
    container_list.append(container_weight)

print()
new_container = int(input('Введите вес нового контейнера: '))
early_container = 200

for i in range(len(container_list)):
  if early_container > new_container > container_list[i]:
    print('Номер, куда встанет новый контейнер:', i + 1)

  early_container = container_list[i]
