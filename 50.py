n = int(input("Сколько чисел будет введено? "))

total = 0

for i in range(n):
    number = int(input("Введите число: "))
    
    if i % 2 == 0:
        total += number  # чётные индексы (0, 2, 4...) — прибавляем
    else:
        total -= number  # нечётные индексы (1, 3, 5...) — вычитаем

print(total)