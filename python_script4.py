class Road:
    def __init__(self, length, width):
        self.length = _length
        self.winth = _winth
    def trassa1(self):
        self.length = _length
        _length = kilometrs
    def trassa2(self):
        self.winth = _winth
        _winth = metrs

class Road1(Road):
    def trassa1(self):
        self.lingth = _length

class Road2(Road):
    def trassa2(self):
        self.winth = _winth

a = 20
# winth, metrs.
b = 5000
# length, metrs.
c = 25
# kilogramm.
d = 5
# santimetrs.
def my_func(a, b, c, d):
    try:
        a = int(input("Введите значение ширины полотна: "))
        b = int(input("Введите значение длины полотна: "))
        c = int(input("Введите массу асфальта в килограммах: "))
        d = int(input("Введите толщину полотна в сантиметрах: "))
    except zerodivisionerror:
        return
    s = a * b * c * d
    return s

print(my_func(a, b, c, d))

