"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
set1 = set()
for i in testList:
    if type[i] == list or type[i] == dict or type[i] == set:
        print(False, i)
    else:
        set1.add(1)
        print(True)
print(set1)
