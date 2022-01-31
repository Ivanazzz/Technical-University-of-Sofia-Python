# Task 1
# Напишете програма на Python, за да получите следващия ден от дадена дата (въведена от потребителя).
# Пример:
# Input a year: 1974 
# Input a month [1-12]: 2 
# Input a day [1-31]: 15 
# The next date is [yyyy-mm-dd] 1974-2-16.

year_input = int(input("Input a year: "))
month_input = int(input("Input a month[1-12]: "))
day_input = int(input("Input a day[1-31]: "))

day_output = day_input + 1
year_output = year_input
month_output = month_input

if month_input == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if day_output > 31:
        day_output = 1
        month_output = month_input + 1
        if month_output > 12:
            year_output = year_input + 1
            month_output = 1

if month_input == 4 or 6 or 9 or 11:
    if day_output > 30:
        day_output = 1
        month_output = month_input + 1

if month_input == 2:
    if year_input % 4 == 0:
        if day_output > 29:
            day_output = 1
            month_output = month_input + 1
    else:
        if day_output > 28:
            day_output = 1
            month_output = month_input + 1
        

print(f"The next date is {year_output}-{month_output}-{day_output}")

    


# Task 2
# Да се състави програма на Python, която дефинира клас Travel с полета: ID, Destination, Flight, Price. 
# Да се добави метод „Reduce“, чрез който всички стойности от полето Price по-големи от 200 да бъдат заменени 
# със стойност по-ниска с 10%. Да се добави и методът Print, чрез който да се отпечатят ID, Destination, Flight, Price.

class Travel():
    def __init__(self, ID, Destination, Flight, Price):
        self.id = ID
        self.destination = Destination
        self.flight = Flight
        self.price = Price

    def reduce(self):
        if self.price > 200:
            self.price -= self.price * 0.1
            return self.price
        else:
            return self.price

    def print_info(self):
        print(f"Information: \n ID: {self.id}\n Destination: {self.destination}\n Flight: {self.flight}\n Price: {self.reduce()}\n")


object1 = Travel(123123123, "Turkey", 18, 180) 
object1.print_info()
object2 = Travel(456456456, "Bulgaria", 9, 270) 
object2.print_info()

