# Exercise 1 
# Напишете програма, която дава възможност на потребителя да въвежда неограничен брой цели числа. 
# Да се изведе какъв е процента на числата, които са кратни на 7, резултата да се закръгли до втория 
# знак след десетичната запетая. Да се изведе каква е сумата на числата, които не са кратни на 7. 
# Да се изведе максималното число измежду всички числа. Да се намери средноаритметичното на числата 
# кратни на седем, резултата да се закръгли до втория знак след десетичната запетая.

from sys import maxsize

sevens_sum = 0
sevens_count = 0
max_num = - maxsize
not_sevens_sum = 0;
total_numbers_count = 0

while True:
    number = input()
    if number.lower() != "stop":
        number = int(number)
        total_numbers_count += 1

        if number % 7 == 0:
            sevens_sum += number
            sevens_count += 1
            if number > max_num:
                max_num = number
        else:
            not_sevens_sum += number
            if number > max_num:
                max_num = number
    else:
        break

percent_divided_by_seven = sevens_count / total_numbers_count * 100  
average_numbers_divided_by_seven = sevens_sum / sevens_count

print(f"{percent_divided_by_seven:.2f}")
print(f"{not_sevens_sum}")
print(f"{max_num}")
print(F"{average_numbers_divided_by_seven:.2f}")



# Exercise 2
# Да се напише програма, която реализира играта „познай числото“ : потребителя въвежда цяло число в 
# интервала от 1 до 10. Програмата също генерира едно случайно число. Ако потребителя е въвел същото 
# число, което е генерирано от програмата се принтира съобщение : „Позна числото“, в противен случай 
# се принтира съобщение : „Съжалявам не позна“. И така продължава този процес на въвеждане на число 
# докато потребителя не въведе 0, нулата е знак за край на играта. След като приключи играта на екрана 
# да се принтира общия брой опити на потребителя, както и броя на познатите числа.

import random

total_numbers_count = 0
guessed_numbers_count = 0

while True:
    generated_num = random.randrange(1, 11)
    number = int(input("Enter number between 1 - 10 or 0 to quit: "))
    total_numbers_count += 1

    if number == 0:
        break
    else:
        if number == generated_num:
            guessed_numbers_count += 1
            print("Позна числото")
        else:
            print("Съжалявам не позна")

print(f"Брой опити: {total_numbers_count}")
print(f"Брой познати числа: {guessed_numbers_count}")
    


# Exercise 3
# Сезона за каране на ски е вече тук. Сформира се голяма група приятели, които  възнамеряват да отидат на ски почивка. 
# Някои от тях се нуждаят от подновяване на  екипировката си. Ето защо първоначално трябва да се прочете броя на скиорите,
# които ще купят екипировка. След това на отделни редове  получаваме броя на якета, каски и ски обувките, които ще 
# бъдат закупени от един скиор. Трябва да се има предвид следния ценоразпис: 
# • Якета - 120 лв. 
# • Каски – 75 лв. 
# • Комплект обувки – 299,90 лв. 
# Към крайната сума се начислява допълнително 20% ДДС. Да се напише програма,  която изчислява общата сумата, 
# която скиорите трябва да заплатят( парите, които скиорите трябва да платят, форматирани до втория знак след  десетичната запетая) .
# Забележка: Един скиор съвсем спокойно може да закупи повече от 1 яке, каска или комплект обувки 

skier_equipment_amount = int(input("Enter the amount of skiers willing to buy equipment: "))
jacket_for_one_skier =  int(input("Enter the amount of jackets: "))
helmet_for_one_skier = int(input("Enter the amount of helmets: "))
boots_for_one_skier = int(input("Enter the amount of boots: "))

jacket_price = skier_equipment_amount * jacket_for_one_skier * 120
helmet_price = skier_equipment_amount * helmet_for_one_skier * 75
boots_price = skier_equipment_amount * boots_for_one_skier * 299.90
total_price = jacket_price + helmet_price + boots_price
total_price_plus_dds = total_price + total_price * 0.2
print(f"{total_price_plus_dds:.2f}")



# Exercise 4
# Напишете програма меню със следните опции:
# - добавяне на студент
# - търсене на студент по език
# - извеждане на информация за всички студенти
# - изход 
# За целта създайте клас Student със полета: номер на студент, име на студент и език за програмиране. 
# Дефинирайте и методи: get_id(self),  get_name(self), get_language(self) , които връщат стойностите на полетата.
# Информацията за студентите се пази в текстов файл.
# Дефинирайте функция Add_student(student),която се използва за добавяне на информация за нов студент в текстов файл. 
# Дефинирайте функция Search(language) за търсене на студент по език. 
# Дефинирайте функция Display() за принтиране на информация за всички студенти .

class Student:
    def __init__(self, id, name, programming_language):
        self.id = id
        self.name = name
        self.programming_language = programming_language

    def get_id(self):
        return f"Student's ID: {self.id}"
    
    def get_name(self):
        return f"Student's name: {self.name}"

    def get_language(self):
        return f"Stuedent's programming language: {self.programming_language}"

def Add_student(student):
    f = open("doc.txt", "a+")
    f.write(f"{student.id}, {student.name}, {student.programming_language}")
    f.close()

student1 = Student(123123123, "Ivan", "Pyhton")
print(student1.get_id())
print(student1.get_name())
print(student1.get_language())
Add_student(student1)
