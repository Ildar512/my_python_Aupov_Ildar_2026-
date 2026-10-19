n = int(input("Сколько строк будет введено? "))

words = []

for i in range(n):
    words.append(input("Введите слово: "))

print(" ".join(words))