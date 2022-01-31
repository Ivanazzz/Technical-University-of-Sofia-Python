# Exercise 1
# Напишете програма, в която е дефиниран клас със следните характеристики:
# Класът има конструктор, на който се предават две стойности.
# Тези стойности се присвояват на полетата на обекта от дадения клас. 
# В класа трябва да бъде описан метод, при извикването на който се показват стойностите на полетата на класа. 
# Проверете функционалността на класа, като създадете на негова основа няколко обекта.

class First:
    def __init__(self, a, b):
        self.A = a
        self.B = b
    def print_param(self):
        print(self.A)
        print(self.B)

first1 = First(77, 88)
first2 = First("Hello", "World")
first3 = First([1, 2, 3], [4, 5, 6])

first1.print_param()
first2.print_param()
first3.print_param()



# Exercise 2
# Напишете програма, в която е описан клас. Обектите на класа трябва да имат поле, представляващо числов списък. 
# Този списък се формира на основата на списък, предаден като аргумент на конструктора. 
# При това от списъка аргумент в списъка поле се включват само числовите елементи (елементите от други типове се игнорират). 
# Също така трябва да се дефинират два метода:
# Първият метод показва съдържанието на полето списък, а вторият метод изчислява средната стойност на елементите на полето списък.

class Second:
    def __init__(self, list):
        self.L1 = []
        for i in list:
            if type(i) is int:
                self.L1.append(i)
    
    def print_list(self):
        for i in self.L1:
            print(i)

    def average(self):
        x = sum(self.L1) / len(self.L1)
        print(x)

y = Second([1, 2, "Hello",  3, 4, "World", 5])
y.print_list()
y.average()



# Exercise 3
# Дефинирайте клас Shape с едно поле задаващо вида на фигурата.
# Дефинирайте клас Square и клас Circle,които наследяват Shape.
# Класът Square и класът Circle  имат предефинирана функция __init__, която приема дължина(радиус)като аргумент.
# И трите класа имат функция за намиране на лице,като лицето на Shape е 0 по подразбиране .
# Потребителя въвежда вида на фигурата и на тази база се създава обект от съответния клас.
# След това се извиква метода за намиране на лице за съответния обект.

import math

class Shape:
    def __init__(self, type):
        self.Type = type

    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght):
        super().__init__(type)
        self.Lenght = lenght
    
    def Area(self):
        a = self.Lenght * self.Lenght
        return a

        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(type)
        self.Radius = radius
    
    def Area(self):
        a = math.pi * self.Radius * self.Radius
        return a

a = input("Enter shape: ")

if a.lower() == "square":
    square1 = Square(12)
    print(square1.Area())
elif a.lower() == "circle":
    circle1 = Circle(7)
    print(circle1.Area())
