summa = int(input('ввод суммы = '))
time = int(input('время:'))
if time >= 10 and time <= 12:
    print('чек=',summa/2)
elif time >= 20 and time <= 22:
    print('чек=',summa/4)
elif time >= 8 and time <= 10 :
    print(summa)
elif time >= 12 and time <=20:
    print(summa)
else:
    print('закрыто')