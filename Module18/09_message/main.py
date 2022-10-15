string = input('сообщение: ').split()
revers_str = ''

for word in string:
    if word.isalpha():
        revers_str += ''.join(word[::-1]) + ' '
    else:
        for i in word:
            if i.isalpha() == False and word[word.index(i)-1::-1].isalpha() and word[:word.index(i):-1].isalpha():
                revers_str += ''.join(word[word.index(i) - 1::-1] + i + word[:word.index(i):-1])
                break
            elif i.isalpha() == False and word[word.index(i) - 1::-1].isalpha():
                revers_str += ''.join(word[word.index(i) - 1::-1] + i)
            elif i.isalpha() == False:
                revers_str += ''.join(i)
        revers_str += ' '

print('Новое сообщение:', revers_str)
