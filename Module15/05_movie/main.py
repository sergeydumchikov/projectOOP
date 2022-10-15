films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []
number = len(films)

while True:
    flick = str(input('Введите понравившейся фильм: '))
    if flick == films:
        break
    elif flick in favorite_films:
        print('уже добавляли')
    elif flick in films:
        favorite_films.append(flick)
    else:
        print('такого фильма нет')

print('Список любимых фильмов:\n', favorite_films)
