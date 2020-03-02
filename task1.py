string = input("Введите текст: ")
length = len(string)
lower = upper = 0

for i in string:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
per_lower = lower / length * 100
per_upper = upper / length * 100
print("%% строчных букв: %.2f%%" % per_lower)
print("%% прописных букв: %.2f%%" % per_upper)