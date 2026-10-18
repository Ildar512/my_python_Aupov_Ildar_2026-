n = int(input("Сколько строк будет введено? "))

for i in range(n):
    text = input("Введите строку: ")
    
    if "плохо" in text:
        continue  # Пропускаем эту строку и переходим к следующей
        
    print(text)