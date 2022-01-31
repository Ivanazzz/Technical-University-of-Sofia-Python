# Exercise 1
# Напишете програма която на основата на текст, въведен от потребителя се създава нов текст,
# в който в сравнение с изходния, думите за разположени в обратен ред

text = input('Enter text: ')
new = text.split() 
new.reverse() 
x = ' '.join(new)  
print(x)



# Exercise 2
# Напишете програма, в която се използва речник. 
# Ключовете в речника са фамилии на писатели, а стойностите – имената на произведения, написани от тях. 
# В програмата се обхождат стойностите на всички елементи в речника и за всяка от тях(име на произведение)  
# потребителя въвежда фамилия на автора.След обхождане на съдържанието на речника и получаването на всички отговори, 
# програмата показва на потребителя броя на правилните отговори.

books = {
    'Zusak' : 'The Book Thief', 
    'Christie' : 'And Then There Were None',
    'Doyle' : 'A Study in Scarlet',
    'Wilde' : 'The Picture of Dorian Gray'
}
count = 0

for i in books.keys():  # тук обхождаме авторите
    print(books[i]) # тук ще ни принтитра името на книгата
    x = input("Enter author's last name: ")
    if x == i:
        count += 1

print(f"Correct: {count}")



# Exercise 3
# Напишете програма, в която на основата на текст, въведен от потребителя, се създава кортеж.
# На основата на този кортеж се създава нов кортеж, в него се включват равноотстоящите елементи, започвайки
# от първия(с нулев индекс). Разстоянието между елементите се въвежда от потребителя.
# Пример:
# Enter string: devetstotin
# ('d', 'e', 'v', 'e', 't', 's', 't', 'o', 't', 'i', 'n')
# Enter distance: 2
# ('d', 'v', 't', 't', 't', 'n')

text = input('Въведи текст: ')
tuple1 = tuple(text)
distance = int(input('Въведи разстояние между елементите: '))
tuple2 = tuple1[::distance]
print(tuple2)



# Exercise 4
# Напишете програма, в която потребителят въвежда две числа, а програмата определя цифрите,
# които са общи в представянията на двете числа.

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
set1 = set(number1)
set2 = set(number2)
set3 = set()

for i in set1:
    for j in set2:
        if i == j:
            set3.add(i)
print(set1)
print(set2)
print(set3)


