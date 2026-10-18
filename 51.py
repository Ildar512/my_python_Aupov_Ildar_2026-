n = int(input("Сколько строк будет введено? "))

found = False

for i in range(n):
    text = input("Введите строку: ")
    
    if "кот" in text or "Кот" in text:
        found = True
        break  # можно прервать, так как условие уже выполнено

if found:
    print("МЯУ")
else:
    print("НЕТ")