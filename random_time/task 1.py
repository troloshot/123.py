"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""


import time


def shahmaty_kek():
    t = time.monotonic()
    start = round(time(), 0)
    while time.monotonic() - t != 0:
        user_input = input('Enter: ')
        if user_input != 'off':
            check_time = round(time(), 0)
            left = (1800 - (check_time - start)) / 60
            print('Осталось:', round(left, 2), 'мин')
        else:
            break


shahmaty_kek()