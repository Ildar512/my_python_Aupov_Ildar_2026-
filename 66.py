m = int(input("Сколько листков посещаемости? "))

# Считываем первый листок и создаём множество "всех присутствовавших"
k = int(input())
all_present = set()
for i in range(k):
    all_present.add(input())

# Считываем остальные листки и оставляем только тех, кто есть в обоих множествах
for sheet in range(1, m):  # от 1 до m-1
    k = int(input())
    current_sheet = set()
    for i in range(k):
        current_sheet.add(input())
    
    # Пересечение: оставляем только тех, кто был на обоих уроках
    all_present = all_present & current_sheet

# Выводим результат
for name in all_present:
    print(name)