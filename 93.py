n = int(input("Сколько строк будет введено? "))

strings = []

for i in range(n):
    strings.append(input("Введите строку: "))

# Встроенная функция sorted() возвращает НОВЫЙ отсортированный список
sorted_strings = sorted(strings)

for text in sorted_strings:
    print(text)