number = int(input())
list = []
tuple = ()

while number != 0:
    num = number % 10
    list.append(num)
    number = number // 10

tuple = (list)
print(tuple)
tuple = (list[::-1])
print(tuple)
