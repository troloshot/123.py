"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""


def gen():
    for i in range(0, 101):
        if i % 11 == 0:
            yield i


def main():
    result= gen()
    for i in result:
        print(i)


main()