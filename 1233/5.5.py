numbers = input('список чисел:').split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

if len(numbers) == 1:
    print('нет')
else:
    for j in range(len(numbers)-1):
        if numbers[j+1] - numbers[j] != 1:
            print("Нет")
            break
    else:
        print("Да")



