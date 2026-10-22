n = int(input("Сколько строк будет введено? "))

# Создаём список для хранения кортежей
result = []

for i in range(n):
    text = input("Введите строку: ")
    # Создаём кортеж из длины строки и самой строки, и добавляем в список
    result.append((len(text), text))

# Выводим каждый кортеж
for item in result:
    print(item)