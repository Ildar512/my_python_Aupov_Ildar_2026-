n = int(input("Сколько строк будет введено? "))

unique_words = set()

for i in range(n):
    text = input("Введите слово: ")
    unique_words.add(text)

print(len(unique_words))