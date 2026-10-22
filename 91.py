n = int(input("Сколько чисел будет введено? "))

numbers = []
for i in range(n):
    numbers.append(int(input("Введите число: ")))

# Отделяем последнее число от остальных
target = numbers[-1]
other_numbers = numbers[:-1]

found = False

# Перебираем все возможные пары с помощью вложенного цикла
for i in range(len(other_numbers)):
    for j in range(i + 1, len(other_numbers)):
        if other_numbers[i] * other_numbers[j] == target:
            found = True
            break  # Нашли пару — дальше искать не нужно
            
    if found:
        break  # Выходим из внешнего цикла, если уже нашли

if found:
    print("ДА")
else:
    print("НЕТ")