# Exercise 1 
# Напишете програма, в която се създават два списъка с еднакви размери. На основата на тези списъци
# се формира нов списък, като в него се поставят чрез редуване елементите от първия и елементите от втория списък.

import random

first_list = []
second_list = []
mixed_list = []
a = 10
n = 0 
s = 0
p = 0

while n < a:
    first_list.append(random.randint(1, 100))
    n += 1
print(first_list)

while s < a:
    second_list.append(random.randint(1, 100))
    s += 1
print(second_list)

x = 0
y = 0

while p < 10:
    mixed_list.append(first_list[x])
    mixed_list.append(second_list[y])
    x += 1
    y += 1
    p += 1

print(mixed_list)



# Exercise 2 
# Напишете програма, в която потребителят запълва списък с числа. После се създава втори списък, който се състои
# от два елемента: стойността на най-големия елемент в списъка и индекса на този елемент в списъка.

first_list = []
second_list = []
count = 0

n = int(input("Enter the lenght of the list: "))

while count < n:
    numbers = int(input("Enter numbers: "))
    first_list.append(numbers)
    count += 1
print(first_list)

x = max(first_list)
y = first_list.index(max(first_list))
second_list.insert(0, x)
second_list.insert(1, y)

print(second_list)



# Exercise 3
# Напишете програма, в която се създава числов списък. Той се запълва със случайни числа. Елементите с четни
# индекси се сортират по възходящ ред, а елементите с нечетни индекси се сортират в низходящ ред.
# Принтирайте новия списък.

import random

list1 = []
list2 = []
list3 = []
result = []

n = 0
while n < 10:
    list1.append(random.randint(1,100))
    n += 1
print(list1)

for i in list1:
    if i % 2 == 0:
        list2.append(i)
    if i % 2 != 0:
        list3.append(i)
    
result = list2 + list3
print(result)
  

