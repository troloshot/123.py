"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class Person:

    def krya_krya(self):
        print('крякаю')

    def wear_clothes(self):
        print('штаны мое все')


class Duck:

    def krya_krya(self):
        print('КРЯ!!!')

    def wear_clothes(self):
        print('Я тип утка КРЯЯЯЯЯЯ!')


def main():
    my_list = [Person(), Duck()]
    for i in my_list:
        i.krya_krya()
        i.wear_clothes()


main()