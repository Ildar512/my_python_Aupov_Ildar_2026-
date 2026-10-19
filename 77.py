text = input("Введите строку: ")

# Создаём список из кодов символов, превращая их в строки для join
codes = [str(ord(char)) for char in text]

# Склеиваем через запятую с пробелом
print(", ".join(codes))