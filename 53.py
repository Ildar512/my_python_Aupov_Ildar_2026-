count = 0
cat_line = -1

while True:
    text = input("Введите строку: ")
    if text == "СТОП":
        break
        
    count += 1  # Увеличиваем счётчик строк
    
    # Если кота ещё не нашли (cat_line == -1) и в строке есть кот
    if cat_line == -1 and ("кот" in text or "Кот" in text):
        cat_line = count

print(cat_line)