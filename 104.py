numbers = input("Введите числа через пробел: ").split()

# Создаём новый список, проходя по всем элементам
result = []

for num_str in numbers:
    num = int(num_str)
    
    # Проверяем, что число нечётное
    if num % 2 != 0:
        square = num ** 2
        # Проверяем, что квадрат не заканчивается на 9
        if square % 10 != 9:
            result.append(str(square))  # сохраняем как строку для join

# Выводим результат через пробел
print(" ".join(result))