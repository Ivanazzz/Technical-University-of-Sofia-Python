# Exercise 1
# Напишете програма, която намира  лицето на геометрична фигура като първо се въвежда вида на фигурата:
# 1- квадрат
# 2-правоъгълник
# 3- прав.триъгълник
# За пресмятане на лицето на отделните фигури да се напишат подходящи функции.


def square(a):
    area = a*a
    return area

def rectangle(a, b):
    area = a*b
    return area

def triangle(a, h):
    area = (a*h)/2
    return area

x = input("Enter shape: ")

if x.lower() == "square":
    a = int(input("Enter a: "))
    square(a)
elif x.lower() == "rectangle":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    rectangle(a, b)
elif x.lower() == "triangle":
    a = int(input("Enter a: "))
    h = int(input("Enter h: "))
    triangle(a, h)



# Exercise 2
# Напишете потребителска функция, проверяваща дали число е палиндром.
# Функцията получава като аргумент число, връща като резултат 1, ако числото е палиндром и 0 ако числото не е палиндром.
# Пример: 121

def palindrom():
    x = input("Enter number: ")
    y = x[::-1]
    if x == y:
        return(bool(True))
    else:
        return(bool(False))

print(palindrom())



# Exercise 3
# Програма, която реализира калкулатор за цели числа. Действията които изпълнява са :
# Събиране +
# Изваждане –
# Умножение *
# Деление /
# Потребителя въвежда вида на операцията.
# После въвежда две числа и резултата се извежда на екрана . Реализирайте отделни функции за отделните операции.

operation = input("Choose operation(add, subtract, multiply, devide): ")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def devide(a, b):
    if b == 0:
        return("You can't devide by zero")
    else:
        return a/b

if operation.lower() == "add":
    print(add(a, b))
elif operation.lower() == "subtract":
    print(subtract(a, b))
elif operation.lower() == "multiply":
    print(multiply(a, b))
elif operation.lower() == "devide":
    print(devide(a, b))