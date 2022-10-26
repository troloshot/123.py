"""
Функция sorted принимает в качестве дополнительного параметра key(Можете почитать документацию).
С помощью lambda-функции отсортируйте этот список словарей по именам
"""


grades = [{'name': 'Jennifer', 'final': 95}, {'name': 'David', 'final': 92}, {'name': 'Aaron', 'final': 98}]
print(sorted(grades, key=lambda x: x['name']))