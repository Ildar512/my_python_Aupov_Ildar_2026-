n = int(input("Сколько чисел будет введено? "))

numbers = []

for i in range(n):
    numbers.append(int(input("Введите число: ")))

p = int(input("Введите начальный индекс p: "))
q = int(input("Введите конечный индекс q: "))

# Вычисляем сумму с помощью среза списка
total = sum(numbers[p:q+1])

print(total)