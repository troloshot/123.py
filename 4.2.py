play = input('выбирите развлечение:')
if play == 'game':
    print('играем в Угадай чилсло')
else:
    print('хорошего дня!')
for i in range(1,4):
    chislo = (input('напиши число (off - закончить игру)'))
    if chislo == 'off':
        print('спасибо за игру')
        break
    elif int(chislo) == 5:
        print('вы выйгрываете билет на концерт')
        break
    else:
        print('попробуй еще раз')
