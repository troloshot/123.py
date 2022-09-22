"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"
numbers_dict = {}
for i in range(10):
    numbers_dict[i] = numbers.count(str(i))
print(numbers_dict)
