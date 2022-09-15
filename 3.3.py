tovar1 = int(input('цена первого товара:'))
tovar2 = int(input('цена второго товара:'))
tovar3 = int(input('цена третьего товара'))
summa= tovar1 + tovar2 + tovar3
if tovar1 < tovar2 and tovar2 < tovar3:
    print('акция:',summa/2)
elif tovar1 > tovar2 and tovar2 > tovar3:
    print('акция:',summa/3)
else:
    print('к оплате:', summa)
