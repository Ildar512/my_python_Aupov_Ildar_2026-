n = int(input("Сколько строк будет введено? "))

strings = []

for i in range(n):
    strings.append(input("Введите строку: "))

query = input("Введите поисковый запрос: ")

for text in strings:
    if query in text:
        print(text)