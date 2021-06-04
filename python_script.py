a = 40
b = 1
c = 10
def my_func(a, b, c):
    a = int(input("Введите количество отработанных часов: "))
    b = int(input("Введите значение ставки: "))
    c = int(input("Введите значение премии: "))
    d = (a * b) + c
    return d

print(my_func(a, b, c))

