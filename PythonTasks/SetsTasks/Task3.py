"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
new_set = set()
mag_set = set()
both_set = set()
for i in range(1, 76):
    new_set.add(i)
for i in range(77, 104):
    mag_set.add(i)
for i in range(21, 34):
    both_set.add(i)
print(len((new_set|mag_set)-both_set))