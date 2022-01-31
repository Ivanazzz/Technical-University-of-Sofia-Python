# Exercise 1
# Напишете програма, в която е описан клас и функция, предназначена за създаване на списък от обекти. 
# Обектите на класа трябва да имат поле (предназначено за записване на целочислена стойност). 
# При извикване на функцията се предава като аргумент цяло число, определящо броя на обектите в списъка.
# Полетата на обектите се запълват с цели нечетни числа.

list = []

class First:
    def __init__(self, number):
        self.number = number
    
    def list_of_objects(a):
        for i in range(0, a):
            b = First(i)
            list.append(b)
        return list

count = 5
list_of_objects(count)
print(list)
for i in range(0, 5):
    print(list[i].number)



# Exercise 2
# Дефинирайте  клас Pnone със следните полета : марка, модел, цена, количество. 
# В класа е дефиниран и метод, който принтира стойностите на полетата.
# Създайте функция, която връща списък с обекти от класа Pnone.
# Принтирайте информация за телефона с максимална цена.
# Намерете средноаритметичното от цените на всички телефони в списъка.
# Изведете списък на всички телефони от дадена марка (въвежда се от клавиатурата).

class Phone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
    
    def print_info(self):
        print(self.brand, self.model, self.price, self.quantity)

list = []
def create_objects():
    for i in range(3):
        brand = input("Enter the phone's brand: ")
        model = input("Enter the phone's model: ")
        price = int(input("Enter the price of the phone: "))
        quantity = int(input("Enter the quantity of the phone: "))
        object = Phone(brand, model, price, quantity)
        list.append(object)
    return list

print(create_objects())