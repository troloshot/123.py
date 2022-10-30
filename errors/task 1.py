def error(l):
    for x in l:
        try:
            print(x / 3)
        except TypeError as e:
            print('Невозможно разделить')


lst = ["Максим",12,14,"Олег","100"]
error(lst)