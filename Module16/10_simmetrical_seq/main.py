def palind(num_list):
    reverse_list = []
    for i in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i])
    if num_list == reverse_list:
        return True
    else:
        return False

num = int(input('кол-во чисел: '))
numbers = []
new_num = []
ans = []
for i_num in range(num):
    n = int(input('Число: '))
    numbers.append(n)


for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        new_num.append(numbers[j])
    if palind(new_num):
        for n in range(0, i):
            ans.append(numbers[n])
        ans.reverse()
        break
    new_num = []

print('Последовательность: ', numbers)
print('Нужно приписать чисел: ', len(ans))
print('Список этих чисел: ', ans)