n = int(input("Сколько чисел будет введено? "))

# Создаём список, в котором каждое введённое число умножено на 3
tripled = []

for i in range(n):
    number = int(input("Введите число: "))
    tripled.append(number * 3)

# Выводим элементы списка через пробел
print(*tripled)