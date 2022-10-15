text = str(input('Введите текст: '))
vowels = "аеёиоуэюя"
list_vowels = [i for i in text if i in vowels]
print('Список гласных букв', list_vowels)
print('Длина списка: ', len(list_vowels))