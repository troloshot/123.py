data = input('введите оценки:')
data = data.split()

k5 = data.count("5")
percent = 100 / len(data) * k5
print(percent)

