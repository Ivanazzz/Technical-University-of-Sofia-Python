# Exercise 1
# Напишете програма, в която на основата на текст, въведен от потребителя, се създава нов текст, 
# в който в сравнение с изходния са изтрити най-дългата и най- късата дума.
# Ако такива думи има няколко, изтрива се само първата от тях.

text = input('Enter text: ')
new = text.split()
print(new)
longest_word = max(new, key = len)
shortest_word = min(new, key = len)
new.remove(longest_word)
new.remove(shortest_word)
new_text = ''

for word in new:
    new_text += word + ' '
print(new_text)



# Exercise 2
# Напишете програма, която намира максимална редица от последователни еднакви елементи в списък и ги отпечатва
# Примерен вход: [2,1,1,2,3,3,2,2,2,1]
#          изход: 2,2,2

list = []
x = 0

while x < 10:
    user = int(input('Enter numbers: '))
    list.append(user)
    x += 1
print(list)

count = 1
temp= 1
num = 0

for i in range(len(list) - 1):
    if list[i] == list[i + 1]:
        temp += 1
    else:
        temp = 1
    if temp > count:
        num = list[i]
        count = temp

print(f'{num} '*count)



# Exercise 3
# Напишете програма за намиране на множество числа( в интервала от 1 до 50),
# които се делят или на 3, или на 4, но да не се делят на 3 и 4 едновременно.

list = []
for x in range(1, 51):
    if x%3 == 0 and x%4 != 0:
        list.append(x)
    elif x%3 != 0 and x%4 ==0:
        list.append(x)

set = set(list)
print(set)



# Exercise 4
# Напишете програма, в която се създава числов списък. Той се запълва със случайни числа.
# Елементите с четни индекси се сортират по възходящ ред, а елементите с нечетни индекси  се сортират
# в низходящ ред. Принтирайте новия списък
# Пример:
# Enter count : 7
# [11, 20, 19, 4, 1, 8, 4] #първоначален списък
# [11, 19, 1, 4]   #списък с четни индекси(0,2,4,6...)
# [1, 4, 11, 19]   #сортиран във възходящ ред
# [20, 4, 8]       #списък с нечетни индекси(1,3,5,7...)
# [20, 8, 4]       #сортиран в низходящ ред
# [1, 20, 4, 8, 11, 4, 19]  #обединение на двата списъка

import random

list = []
count = int(input('Enter count: '))
n = 0

while n < count:
    list.append(random.randint(1, 100))
    n += 1
print(list)

even_numbers = []
odd_numbers = []

for i in list:
    if i%2 == 0:
        even_numbers.append(i)
print(even_numbers)
even_numbers.sort()
print(even_numbers)

for i in list:
    if i%2 != 0:
        odd_numbers.append(i)
print(odd_numbers)
odd_numbers.sort(reverse = True)
print(odd_numbers)

print(even_numbers + odd_numbers)
