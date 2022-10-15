max_N = int(input('Введите максимальное число: '))
set_nums = set(range(1, max_N + 1))
ans_set = set()

while True:
    nums = input('Нужное число есть среди вот этих чисел: ')
    if nums == 'Помогите !':
        print('Артём мог загадать следующие числа: ', set_nums)
        break
    nums = nums.split()
    for i in range(len(nums)):
        ans_set.add(int(nums[i]))
    answer = input('Ответ Артема: ')
    if answer == 'Да':
        set_nums = set_nums.intersection(ans_set)
    else:
        set_nums = set_nums.difference(ans_set)
    ans_set = set()

