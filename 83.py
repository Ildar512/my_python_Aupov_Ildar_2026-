n = int(input("Сколько чисел будет введено? "))

numbers = []

for i in range(n):
    numbers.append(int(input("Введите число: ")))

# Создаём список для сумм
sums = []

# Проходим по индексам от 0 до n-2 (не включая последний)
for i in range(n - 1):
    total = numbers[i] + numbers[i + 1]
    sums.append(str(total))  # Сразу превращаем в строку для join

# Выводим результат
print(" ".join(sums))