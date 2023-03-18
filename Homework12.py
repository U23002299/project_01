# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import datetime
import random

three_songs = random.sample(my_favorite_songs, 3, counts = None)

three_songs_time = round(int(three_songs[0][1] + three_songs[1][1] + three_songs[2][1]))
print(three_songs,'\n', f'Три песни звучат: {three_songs_time} минут')

print("Пункт Д:", datetime.time(00, three_songs_time, 00).strftime('%M:%S'))
      
# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

my_favorite_songs_2 = list(my_favorite_songs_dict.items())
another_three_songs = random.sample(my_favorite_songs_2, 3, counts = None)
# print(another_three_songs)
another_three_songs_time = round(int(another_three_songs[0][1] + another_three_songs[1][1] + another_three_songs[2][1]))

print(another_three_songs,'\n', f'Три песни звучат: {another_three_songs_time} минут')

print("Пункт Д:", datetime.time(00, another_three_songs_time, 00).strftime('%M:%S'))

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 


