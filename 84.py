n = int(input("Сколько строк будет введено? "))

strings = []

for i in range(n):
    strings.append(input("Введите строку: "))

# Выводим элементы списка в обратном порядке
for i in range(n - 1, -1, -1):
    print(strings[i])