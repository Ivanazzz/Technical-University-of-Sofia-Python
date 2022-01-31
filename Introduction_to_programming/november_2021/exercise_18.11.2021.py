# Exercise 1 
# На функция се подават два аргумента: списък с числа и число. 
# Променете всички елементи от списъка със стойност по-голяма от даденото число на 0(нула).

import random 

def func1(list, number):
    for i in range(0, len(list)):
        if list[i] > number:
            list[i] = 0
    return list

count = 0
list = []

number = int(input("Enter a number: "))

while count < 10:
        list.append(random.randint(1, 50))
        count += 1
print(list)

print(func1(list, number))


# Exercise 2
# Напишете програма, в която се създава  функция. 
# Функцията получава като аргумент числов списък и връща като резултат друг списък, 
# в който са включени само нечетните числа от списъка аргумент.

import random

def func2(list):
    for i in list:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

new_list =[]
list = []
count = 0

while count < 10:
    list.append(random.randint(1, 50))
    count += 1
print(list)

print(func2(list))


# Exercise 3
# Напишете програма,в която е описана функция, връщаща като резултат второто по големина число в списъка, 
# предаден като аргумент на функцията.

import random

def func3(list):
    list.sort(reverse = True)
    return list[1]


list = []
count = 0
while count < 10:
    list.append(random.randint(1, 50))
    count += 1
print(list)

print(func3(list))



# Exercise 4
# Напишете функция, която проверява дали два стринга въведени от потребителя са анаграма.
# Функцията получава като аргументи два стринга,връща като резултат 1 ако са анаграма и 0 ако не са.
# Примерен вход: "coast "    "stoak "           
# Изход : The strings aren't anagrams.        
# Примерен вход: "stop "    "post " 
# Изход : The strings are anagrams.

def anagram(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return "The strings are anagrams."
    else:
        return "The strings aren't anagrams."

s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")

print(anagram(s1, s2))