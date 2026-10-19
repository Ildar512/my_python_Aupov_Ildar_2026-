text = input("Введите строку: ")

# Создаём множество гласных для быстрой проверки
vowels = set("аеёиоуыэюя")

count = 0

for char in text.lower():  # Переводим в нижний регистр, чтобы 'А' тоже считалась
    if char in vowels:
        count += 1

print(count)