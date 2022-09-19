login = input('Введите логин')
negood = '=?*^$№@_'
for i in range (len(login)):
    if login[i] in negood:
        print(login[i])

