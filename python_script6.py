class Car:
    def __init__(self, speed, color, name, is_police, show_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed = show_speed

def show_speed(self):
        self.show_speed = show_speed
        self.speed = speed

def go(self):
        self.go = go
        self.show_speed = show_speed
        self.speed = speed

def stop(self):
        self.stop = stop
        self.show_speed = show_speed
        self.speed = speed

def turn_direction(self):
        self.turn_direction = turn_direction
        self.show_speed = show_speed
        self.speed = speed

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, show_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed = speed

def show_speed(self):
        self.show_speed = show_speed
        self.speed = speed
        s > 300 == stop

def color(self):
        self.color = color
        color = red

def name(self):
        self.name = name
        name = subaru

def go(self):
        self.go = go
        self.name = name
        name = subaru
        go == 80

def turn_direction(self):
        self.turn_direction = turn_direction
        self.show_speed = show_speed
        self.speed = speed
        turn_direction = right
        right == 170
        turn_direction = left
        left ==130
        turn_direction = back
        back == 90
        turn_direction = forward
        forward ==270

def stop(self):
        self.stop = stop
        self.show_speed = show_speed
        self.speed = speed
        s > 300 == stop

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, show_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed = show_speed

def show_speed(self):
        self.show_speed = show_speed
        self.speed = speed
        s > 200 == stop

def color(self):
        self.color = color
        color = black

def name(self):
        self.name = name
        name = bmv

def go(self):
        self.go = go
        self.show_speed = show_speed
        self.speed = speed
        self.name = name
        name = bmv
        go ==40

def turn_direction(self):
        self.turn_direction = turn_direction
        self.show_speed = show_speed
        self.speed = speed
        turn_direction = right
        right = 170
        turn_direction = left
        left = 120
        turn_direction = back
        back = 60
        turn_direction = forward
        forward = 190

def stop(self):
        self.stop = stop
        self.show_speed = show_speed
        self.speed = speed
        s >200 == stop

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, show_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed = show_speed

def show_speed(self):
        self.show_speed = show_speed
        self.speed = speed
        s > 120 == stop

def color(self):
        self.color = color
        color = grey

def name(self):
        self.name = name
        name = mazda

def go(self):
        self.go = go
        self.show_speed = show_speed
        self.speed = speed
        self.name = name
        name = mazda
        go = 20

def turn_direction(self):
        self.turn_direction = turn_direction
        self.show_speed = show_speed
        self.speed = speed
        turn_direction = right
        right = 100
        turn_direction = left
        left = 90
        turn_direction = back
        back = 50
        turn_direction = forward
        forward = 115

def stop(self):
        self.stop = stop
        self.show_speed = show_speed
        self.speed = speed
        s > 120 == stop

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, show_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed = show_speed

def show_speed(self):
        self.show_speed = show_speed
        self.speed = speed
        s > 90 == stop

def color(self):
        self.color = color
        color = green

def name(self):
        self.name = name
        name = kraz

def go(self):
        self.go = go
        self.show_speed = speed
        self.speed = speed
        self.name = name
        name = kraz
        go = 10

def turn_direction(self):
        self.turn_direction = turn_direction
        self.show_speed = show_speed
        turn_direction = right
        right = 70
        turn_direction = left
        left = 50
        turn_direction = back
        back = 30
        turn_direction = forward
        forward = 85

def stop(self):
        self.stop = stop
        self.show_speed = show_speed
        self.speed = speed
        s > 90 == stop

a = 50
b = 60
c = 70
def my_speed(a, b, c):
    try:
        a = int(input("Введите текущую скорость городской машины: "))
        if a>=60:
            b = input("Вы привысили допустимую скорость: ")
        if a==60:
            c = input("Вы находитесь на максимально разрешенной скорости в данной местности: ")
        if a<=60:
            d = input("Вы едите на допустимой скорости: ")
    except zerodivisionerror:
        return
    return a

print(my_speed(a, b,c))

x = 30
y = 40
z = 50
def my_speed1(x, y, z):
    try:
        f = int(input("Введите текущую скорость рабочей машины: "))
        if f>=40:
            g = input("Вы привысили допустимую скорость: ")
        if f==40:
            h = input("Вы двигаетесь на максимально разрешённой скорости: ")
        if f<=40:
            k = input("Вы двигаетесь на разрешённой скорости: ")
    except zerodivisionerror:
        return
    return f

print(my_speed1(x, y, z))


































