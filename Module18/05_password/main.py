def nums_fun():
    count_letter = 0
    for i_elem in password:
        if i_elem.isdigit() == True:
            count_letter += 1
    if count_letter >= 3:
        return True

def letter_up():
    for i_let in password:
        if i_let.isupper() == True:
            return True

def numpass():
    if len(password) >= 8:
        return True

while True:
    password = input('Придумайте пароль: ')
    if (numpass() and nums_fun() and letter_up()) == True:
        print('Это надежный пароль')
        break
    else:
        print('Пароль ненадежный. Попробуйте снова')






