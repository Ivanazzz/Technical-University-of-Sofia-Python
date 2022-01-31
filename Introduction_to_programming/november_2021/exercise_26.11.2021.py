# Exercise 1 
# Напишете програма, в която е описана функция, която проверява дали едно цяло число е просто, 
# числото се предава като аргумент на функцията. Функцията връща резултат 1 ако числото е просто и 0,
# ако числото не е просто. Да се принтират всички прости числа в интервала от 2 до това число.

def number(x):
    if x == 1:
        return 0
    else:
        count = 0
        for i in range(1, x + 1):
            if x % i == 0:
                count += 1
        if count > 2:
            return 0
        else:
            return 1

print(number())




# Exercise 2 
# Програма английско-български речник, запълнен речник със стойности. Потребителя прави своя избор, който може да е:
# - търсене на дума в речника
# - добавяне на дума
# - изтриване на дума
# - показване на всички думи в речника.
# Програмата продължава докато не се въведе символа q - изход .
# За всяка една от опциите реализирайте отделни функции.

def search(dictionary):
    en = input("Enter english word for search: ")
    return dictionary.get()

def add():
    en_word = input("Enter the english word: ")
    bg_word = input("Enter the bulgarian word: ")
    new_word = {en_word: bg_word}
    dictionary.update(new_word)

def delete():
    key = input("Enter the word you want to delete: ")
    if key in dictionary.keys():
        dictionary.pop(key)
def show():
    return dictionary

dictionary = {
    "cat": "котка",
    "dog": "куче",
    "frog": "жаба"
}

command = input("What function do you choose(search, add, delete, show, q(quit)): ")
while command.lower() != "q":
    if command.lower() == "search":
        print(search())
    elif command.lower() == "add":
        add()
    elif command.lower() == "delete":
        delete()
    elif command.lower() == "show":
        print(show())
    command = input("What function do you choose(search, add, delete, show, q(quit)): ")




# Exercise 3
# Напишете програма, която отпечатва перфектните числа от даден списък с цели числа. 
# Програмата включва функция, която получава като аргумент число и принтира числото, ако то е перфектно.
# Примерен вход: [14, 20, 6, 78, 28]
# Изход: 6, 28
# 28=1+2+4+7+14                1,2,4,7,14 са делителите на числото  28

def perfect_number():
    times = int(input("Enter how many numbers do you want to insert: "))
    n = 0
    list = []
    perfect_numbers = []

    while n < times:
        number = int(input("Enter number: "))
        list.append(number)
        n += 1

    for num in range(0, len(list)):
        sum = 0
        for i in range(1, list[num]):
            if list[num] % i == 0:
                sum += i
        if sum == list[num]:
            perfect_numbers.append(str(sum))
    output = ", ".join(perfect_numbers)

    print(output)

perfect_number()
