n = int(input("Сколько чисел будет введено? "))

total = 0

for i in range(n):
    number = int(input("Введите число: "))
    
    if number <= 0:
        continue  # Пропускаем нули и отрицательные числа
        
    total += number

print(total)