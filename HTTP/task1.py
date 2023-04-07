"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""
import requests
def random_cats_pictures():
    for i in range(2):
        my_file = open(f'Кот_рандомный{i}', 'wb')
        my_file.write(requests.get('https://cataas.com/cat').content)

def random_cats_pictures_origin():
    for i in range(2):
        my_file = open(f'Кот_оригинальный{i}', 'wb')
        my_file.write(requests.get('https://cataas.com/cat?type=original').content)

def random_cats_pictures_pixel():
    for i in range(2):
        my_file = open(f'Кот_пиксельный{i}', 'wb')
        my_file.write(requests.get('https://cataas.com/cat?filter=pixel').content)

random_cats_pictures()
random_cats_pictures_origin()
random_cats_pictures_pixel()
