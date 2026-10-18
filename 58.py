cat_found = False

while True:
    text = input("Введите строку: ")
    if text == "СТОП":
        break
    
    # Если в строке есть кот, фиксируем находку
    if "кот" in text or "Кот" in text:
        cat_found = True
        
    # Если в строке есть пёс, кот теряется (сбрасываем флаг)
    if "пёс" in text or "Пёс" in text:
        cat_found = False

if cat_found:
    print("МЯУ")
else:
    print("НЕТ")