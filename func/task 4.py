"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""


def imt(weight, height):
    Imt = (weight / (height * height)) * 10000
    print('Ваш ИМТ = ', Imt)
    print(imt_result(Imt))


def imt_result(Imt_):
    if Imt_ < 18.5:
        return 'Недостаточный вес'
    elif 18.5 <= Imt_ <= 25:
        return 'ИМТ в норме'
    elif Imt_ > 25:
        return 'Избыточный вес'


imt(int(input('введите вес: ')), int(input('введите рост: ')))


