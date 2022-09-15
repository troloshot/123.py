kategor = input('категория товаров:')
summa = int(input('сумма ='))
if kategor == 'продукты':
    print('отлично')
    if summa >=0 and summa < 100:
        print('попробуйте нашу выпечку!')
    elif summa >= 100 and summa < 500:
        print('как насчет орехов в шоколаде?!')
    else:
        print('порпробуйте экзотичесике фрукты!')
if kategor != 'продукты':
    if kategor != 'продукты':
        print('загляните в товары для дома!')