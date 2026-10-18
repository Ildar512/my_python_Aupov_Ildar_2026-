first_list = set()
second_list = set()

# Считываем первый список до пустой строки
while True:
    text = input("Введите число для 1-го списка (Enter — конец): ")
    if text == "":
        break
    first_list.add(text)

# Считываем второй список до пустой строки
while True:
    text = input("Введите число для 2-го списка (Enter — конец): ")
    if text == "":
        break
    second_list.add(text)

# Ищем пересечение множеств
common = first_list & second_list

if common:
    print(" ".join(common))
else:
    print("EMPTY")