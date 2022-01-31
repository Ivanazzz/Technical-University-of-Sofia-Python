# Да се създаде програма, която да чете предварително създаден текстов файл и да извежда 
# съдържанието му ред по ред с използването на for цикъл.

f = open("file.txt", "r")
for line in f:
    print(line)

f.close()

# Да се създаде двоичен файл с име “document.bin”. Създаденият файл да се отворен и се реализира 
# запис в режим „wb“ на стринга „This is good“,

s = open("document.bin", "wb")
text = "This is good"
text1 = text.encode("utf-8")
s.write(text1)
s.close()

s = open("document.bin", "rb")
print(s.read())
s.close()