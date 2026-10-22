text = input("Введите текст: ")

# Разбиваем строку на слова по пробелам
words = text.split()

# Идём по индексам с шагом 3, начиная со 2-го элемента (индекс 2)
for i in range(2, len(words), 3):
    print(words[i])