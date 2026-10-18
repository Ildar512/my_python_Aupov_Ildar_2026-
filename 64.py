m = int(input("Сколько учеников изучают английский? "))
english = set()

for i in range(m):
    english.add(input("Введите фамилию (английский): "))

n = int(input("Сколько учеников изучают немецкий? "))
german = set()

for i in range(n):
    german.add(input("Введите фамилию (немецкий): "))

# Симметричная разность: элементы, которые есть только в одном из множеств
only_one = english ^ german

if only_one:
    print(len(only_one))
else:
    print("NO")