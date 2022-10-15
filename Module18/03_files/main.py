sring = input('Название файла: ')
special_sym = '@ № $ % ^ & * ( )'.split()
if sring[0] in special_sym:
    print('Ошибка: название начинается на один из специальных символов')
elif (sring.endswith('.txt') or sring.endswith('.docx')) == False:
    print('Ошибка раcширения')
else:
    print('Файл назван верно')