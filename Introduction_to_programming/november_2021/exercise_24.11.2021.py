# Exercise 1
# Да се напише код на Python, който дефинира клас Person с полета име (name), фамилия (family), 
# възраст (age), националност (nationality). Да се дефинира конструктор, който инициализира полетата на класа. 
# Да се добави метод print_info, който отпечатва имената и националността на съответното лице. 
# Да се създадат обекти-инстанции на класа. За тях  да се извика методът print_info.

class Person:
    def __init__(self, name, family, age, nationality):
        self.Name = name
        self.Family = family
        self.Age = age
        self.Nationality = nationality
    def print_info(self):
        print(f"Info: Name: {self.Name}, Nationality: {self.Nationality}")

person1 = Person("Ivan", "Ivanov", 21, "Bulgarian")
person1.print_info()



# Exercise 2
# Да се добави към кода от Задача 1 клас Student, наследник на класа Person с две нови полета – университет (university)
# и година на обучение (yearofstudy). Да се предифинира за него методът print_info, така, че да отпечатва и тези две полета. 
# Да се създадат инстанции на новия клас и за тях да се извика методът print_info.

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.University = university
        self.Yearofstudy = yearofstudy
    def print_info(self):
        print(f"Info: Name: {self.Name}, Nationality: {self.Nationality}, University: {self.University}, Year of study: {self.Yearofstudy}")

student1 = Student("Peter", "Pavlov", 22, "Bulgarian", "TU-Sofia", 2)
student1.print_info()



# Exercise 3
# Да се добави към кода от Задача 1 и Задача 2 клас Lecturer, наследник на класа Person с две нови полета – 
# университет (university) и опит (experience) – брой години преподавателски стаж. 
# Да се предифинира за него методът print_info, така, че да отпечатва тези две полета. 
# Да се създадат инстанции на новия клас и за тях да се извика методът print_info.

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.University = university
        self.Experience = experience
    def print_info(self):
        print(f"Info: Name: {self.Name}, Nationality: {self.Nationality}, University: {self.University}, Experience: {self.Experience}")

lecturer1 = Lecturer("Daniel", "Kolev", 34, "Bulgarian", "TU-Sofia", 13)
lecturer1.print_info()