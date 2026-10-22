n = int(input("Сколько строк будет введено? "))

strings = []

for i in range(n):
    strings.append(input("Введите строку: "))

# Сортируем с помощью параметра key
sorted_strings = sorted(strings, key=lambda x: (len(x), x))

for text in sorted_strings:
    print(text)