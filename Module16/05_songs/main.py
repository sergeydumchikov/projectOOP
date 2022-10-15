violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def music(sublist):
    for elem in sublist:
        if isinstance(elem, float):
            return elem


number_songs = int(input('Сколько песен выбрать? '))
summ = 0

for song in range(number_songs):
    print('Название', song + 1, 'песни: ', end='')
    name_sound = str(input(''))
    for name in violator_songs:
        if name_sound in name:
            summ += music(name)



print('Общая продолжительность песен:', summ)
