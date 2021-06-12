class Worker:
    def __init__(self, name, surname, position, incone):
        self.name = name
        self.surname = surname
        self.position = position
        self.incone = _incone

class Position(Worker):
    def __init__(self, get_full_name, get_total_incone):
        self.get_full_name = get_full_name
        self.get_total_incone = get_total_incone
    def position1(self):
        self.get_full_name = get_full_name
        self.name = name
        self.surname = surname
    def position2(self):
        self.get_total_incone = get_total_incone
        self.position = position
        self.incone = _incone
        self.incone_full = {}
    def incone_full(self, incone_full):
        self.incone_full.append(wage)
        self.incone_full.append(bonus)


a = 'name'
b = 'surname'
def my_fullname(a, b):
    try:
        a = input("Введите Ваше имя: ")
        b = input("Введите Вашу фамилию: ")
    except valueerror:
        return
    c = a, b
    return c

print(my_fullname(a, b))


x = 50000
y = 25000
def my_total(x, y):
    try:
        x = int(input("Введите сумму дохода: "))
        y = int(input("Введите сумму бонуса: "))
    except zerodivisionerror:
        return
    z = x + y
    return z

print(my_total(x, y))







