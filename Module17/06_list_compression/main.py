numbers = [1, 0, 4, 5, 0, 2]
compr_list_1 = [i for i in numbers if i != 0]
num = len(numbers) - len(compr_list_1)
compr_list_2 = [0 for _ in range(num)]
compr_list = compr_list_1 + compr_list_2
compr_list = [i for i in compr_list_1 if i != 0]

print(compr_list)




