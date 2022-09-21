data = input('введите оценки:')
data = data.split(', ')

for i in range(len(data)):
    data[i] = int(data[i])

k5 = data.count(5)
k4 = data.count(4)
k3 = data.count(3)
func = (k5 + k4 + k3) / len(data) * 100
print('список оценок:',data)
print('5:',k5)
print('4:',k4)
print('3:',k3)
print(func)


