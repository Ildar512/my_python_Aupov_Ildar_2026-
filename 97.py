n = int(input("Сколько чисел будет введено? "))

numbers = []
for i in range(n):
    numbers.append(int(input("Введите число: ")))

# Превращаем список во множество, чтобы убрать дубликаты,
# и снова в список (или просто считаем длину множества)
unique_numbers = set(numbers)

print(len(unique_numbers))