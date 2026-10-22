n = int(input("Введите число: "))

# Используем range(n), чтобы не включать само число n
squares = [i ** 2 for i in range(n)]

print(*squares)