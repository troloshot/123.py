def timetable(reg):
    if 'расп' in reg.lower():
        print('пн 14:30-16:00,'
              'ср 18:30-20:00,'
              'пт 10:30-13:00')


def teatcher(reg):
    if 'трен' in reg.lower():
        print('Зубенко Михаил Петрович')


def sum(reg):
    if 'плат' in reg.lower():
        print('с вас 2500 рублей')


def juice(reg):
    if 'сок' in reg.lower():
        name_juice()
        price()


def name_juice():
    print('ананасовый, яблочный или персиковый? ')


def price():
    a = input('вид сока: ')
    if a == 'ананасовый':
        print('с вас 100 рублей!')
    elif a == 'яблочный':
        print('с вас 80 рублей!')
    elif a == 'персиковый':
        print('вас 90 рублей!')
    else:
        print('спасибо за покупку, хорошего дня!')