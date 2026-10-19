n = int(input("Сколько строк будет введено? "))

strings = []
for i in range(n):
    strings.append(input("Введите строку: "))

word1 = input("Первое слово: ")
word2 = input("Второе слово: ")

for text in strings:
    # Проверяем, что ОБА слова есть в строке одновременно
    if word1 in text and word2 in text:
        print(text)