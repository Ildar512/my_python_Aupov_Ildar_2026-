shift = int(input("Введите шаг сдвига: "))
text = input("Введите строку: ")

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
result = ""

for char in text:
    # Проверяем, является ли символ русской буквой (строчной или заглавной)
    if char in alphabet or char.lower() in alphabet:
        
        # Запоминаем, была ли буква заглавной
        is_upper = char.isupper()
        
        # Работаем с маленькой буквой для удобства
        lower_char = char.lower()
        
        # Находим текущую позицию буквы в алфавите
        index = alphabet.index(lower_char)
        
        # Вычисляем новую позицию по модулю 33
        new_index = (index + shift) % len(alphabet)
        
        # Берём новую букву из алфавита
        new_char = alphabet[new_index]
        
        # Если исходная буква была заглавной, возвращаем ей регистр
        if is_upper:
            new_char = new_char.upper()
            
        result += new_char
    else:
        # Если символ не буква (пробел, цифра, знак препинания), оставляем как есть
        result += char

print(result)