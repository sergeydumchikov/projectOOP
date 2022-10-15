import random
def rand():
    elem = random.uniform(5, 10)
    return elem


fst_comand = [round(rand(), 2) for _ in range(20)]
sec_comand  = [round(rand(), 2) for _ in range(20)]
trt_comand = [max(sec_comand[i], fst_comand[i]) for i in range(20)]

print('Первый список: ', fst_comand)
print('Второй список: ', sec_comand)
print('Победители: ', trt_comand)
