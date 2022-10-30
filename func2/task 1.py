"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def parameters(par='ok', par1=1, par2=[1]):
    if par and par1 and par2:
        print(par, par1, par2)


parameters('asas', 1301, ['sasa', 13])
parameters('', [], 0)