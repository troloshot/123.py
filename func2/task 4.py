"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.
Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""


def calculate(*args):
    list = []
    list1 = []
    for arg in args:
        list.append(arg)
    number = sum(list) / len(list)
    for el in list:
        if el > number:
            list1.append(el)
    result = (number, list1)
    return result


print(calculate(1, 3, 4, 7, 93, 18,))

