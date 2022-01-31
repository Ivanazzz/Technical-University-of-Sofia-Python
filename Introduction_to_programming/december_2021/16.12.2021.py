# Exercise 1

import pickle

test = ["apple", "orange", "cherry"]
with open('list.pickle', 'wb+') as f:
    pickle.dump(test, f)
    pickle.load(f)
        
        

# Exercise 3
# Напишете програма, която намира и принтира най-дългата дума от текстов файл.

f = open("doc.txt", "a+")
f.seek(0)
count = 0
max_word_count = 0
max_word = ""

for line in f:
    for word in line.split():
        count = 0
        for char in range(0, len(word) + 1):
            count += 1
        if count > max_word_count:
            max_word_count = count
            max_word = word

print(max_word)
f.close()