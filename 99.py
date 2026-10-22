n = int(input("Сколько человек? "))

people = []

for i in range(n):
    # Считываем строку и разбиваем на фамилию и рост
    name, height = input("Введите фамилию и рост: ").split()
    # Сохраняем как кортеж: (фамилия, рост)
    people.append((name, int(height)))

# Сортируем по второму элементу кортежа (росту) по убыванию
people.sort(key=lambda x: x[1], reverse=True)

# Выводим результат
for name, height in people:
    print(name, height)