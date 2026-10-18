n = int(input("Сколько чисел будет введено? "))

product = 1

for i in range(n):
    number = int(input("Введите число: "))
    if number != 0:
        product *= number

print(product)