n = int(input("Сколько чисел будет введено? "))

total = 0

for i in range(n):
    number = int(input("Введите число: "))
    total += number

print(total)