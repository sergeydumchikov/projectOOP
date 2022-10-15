text = str(input('Введите строку: '))

index_1 = text.index('h')
index_2 = text.rindex('h')

fst_list = text[:index_1]
sec_list = text[index_2:index_1:-1]
trt_list = text[index_2::]

print(fst_list + sec_list + trt_list)



