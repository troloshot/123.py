"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""
def degrees(temp):
    for i in temp:
        print(f'сегодня {i} градусов')

degrees([1,2,3,4,5,6,7,8])
