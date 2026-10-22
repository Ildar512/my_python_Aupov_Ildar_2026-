n = int(input("Сколько чисел будет введено? "))

numbers = []
for i in range(n):
    numbers.append(int(input("Введите число: ")))

# Алгоритм пузырьковой сортировки
for i in range(n - 1):
    # Внутренний цикл идёт до n - 1 - i, 
    # так как после каждой итерации самый большой элемент "всплывает" в конец
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            # Меняем элементы местами, если они стоят не по порядку
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Выводим результат
for number in numbers:
    print(number)