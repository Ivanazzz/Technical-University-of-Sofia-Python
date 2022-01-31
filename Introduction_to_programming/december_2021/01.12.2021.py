# Exercise 1
# Напишете програмата, в която потребителя въвежда име и възраст. Да се генерира изключение, 
# ако името съдържа цифри и ако възрастта е по-малка от 0 и по-голяма от 100.
# Генерираните изключения да се прихванат и обработят.

try:
    name = input('Enter your name: ')
    for i in "1234567890":
        for j in name:
            if i == j:
                raise ValueError("Your name can't include numbers!")
    age = int(input('Enter your age: '))
    if age < 1 or age > 100:
        raise Exception("Yout age can't be less than zero or greater than 100!")
except ValueError as erorr:
    print(erorr)
except Exception as error:
    print(error)
