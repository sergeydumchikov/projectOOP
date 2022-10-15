list_number = [1, -2, 3, 2, 5]
position = int(input('Сдвиг: '))
print('изначальный сисок:', list_number)
new_list_number = []
number = len(list_number)

for i in range(position):
  for i in range(number):
    if list_number[i] == list_number[number - position]:
      new_list_number.append(list_number[i])
      number += 1
      break
for i in range(len(list_number) - position):
  new_list_number.append(list_number[i])
print('сдвинутый список:', new_list_number)
