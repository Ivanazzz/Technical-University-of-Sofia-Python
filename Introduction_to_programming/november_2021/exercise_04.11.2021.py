# Exercise 1
# Напишете програма , в която потребителя въвежда текст и на негова база се създава речник. За ключове на речника служат символите от текста, а стойността на елементите се определя от броя на съответните символи в текста.
# Примерен вход :  SSWTWWTAAA
# Речникът ще се състои от 4 елемента : А:3     S:2       T:2     W:3text = input('Enter text: ')

text = input('Enter text: ')
dictionary = {}
neshto = set(text)
for i in neshto:
    dictionary[i] = text.count(i)
print(dictionary)



# Exercise 2
# Напишете програма, в която потребителя въвежда чяло число. 
# От него се създава списък състоящ се от числата от 1 до това число .
# Въз основа на този списък се създава речник, в който елементите на списъка служат за ключове на елементите на речника, 
# а стойностите на тези елементи в речника  са елементите на списъка но в обратен ред.
# Пример : ако сме въвели числото 4 , създава се списъка  [1,2,3,4 ] и на негова основа се създава речник с 4 елемента:
# {1:4, 2:3,  3:2,  4:1}

x = int(input('Въведете цяло число: '))
list = []
dict = {}
for i in range(1, x + 1):
    list.append(i)
    dict[i] = x - i + 1
print(list)
print(dict)



# Exercise 3
# Напишете програма, в която потребителя въвежда цяло число, а програмата формира два кортежа, състоящи  се от цифрите ,
# влизащи в това число. Единият  с цифрите на числото в прав ред и втори , в който цифрите са в обратен ред.

x = int(input('Въведете цяло число: '))

y = [int(a) for a in str(x)]
print(y)

y.sort()
tuple1 = tuple(y)
print(tuple1)
y.sort(reverse = True)
tuple2 = tuple(y)
print(tuple2)


# Exercise 4
# Напишете програма, която проверява дали редицата от цели числа a0,a1,....an  се състои от различни елементи.


import random

list = []
n = 0 
p = 0
for x in range(10):
    list.append(random.randint(0, 50))
print(list)

list.sort()
print(list)  # този принт не е включен в условието, но просто ни помага да видим кои са повтарящите се елементи
a = 0
b = 0
c = 0
while a < 10:
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            b += 1
        elif list[i] != list[i + 1]:
            c += 1
    a += 1

if b != 0:
    print('There are somewhere equal elements')
elif c != 0:
    print('There are all diferrent elements')
         
         

    


# Exercise 5
# Напишете програма, в която се създава числов списък. Той  се запълва със случайни числа. 
# След това между всяка двойка елементи от този списък се вмъква нов , равен на сумата от стойностите на съседните елементи.


import random

numbers = []
filtered_data = []
something = []

for x in range(10):
    numbers.append(random.randint(0, 30))
print(numbers)

y = 0
n = 0

while y < 5:
    filtered_data.append(numbers[n] + numbers[n + 1])
    n += 2
    y += 1
print(filtered_data)

something = numbers

s = 0
a = 1
b = 0

while s < 5:
    something.insert(a, filtered_data[b])
    a += 3
    b += 1
    s += 1
print(something)
