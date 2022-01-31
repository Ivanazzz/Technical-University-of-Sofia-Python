# Exercise 1
for x in range(ord('a'), ord('z')+1):
    print(chr(x))



# Exercise 2
n = int(input("n= "))
suma = 0
while n != 0:
    suma += n % 10
    n//=10
print(suma)



# Exercise 3

a = float(input("Въведтете максималната стипендия във Вашия университет:"))
b = float(input("Въведете Вашият успех:"))
c = 0
if b >= 5.50 and b <= 6.00:
    c = a
    print(f"Стипендията Ви е: {c}")
elif b >= 5.00 and b < 5.50:
    c = a * 0.7
    print(f"Стипендията Ви е: {c}")
elif b >= 4.50 and b < 5.00:
    c = a / 2
    print(f"Стипендията Ви е: {c}")
elif b < 4.50:
    print("Не получавате стипендия")
else: print ("Неправилно въведени данни!!!")