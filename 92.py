n = int(input("Сколько учеников? "))

students = []

# Считываем пары и сохраняем их как список строк (или кортежей)
for i in range(n):
    line = input("Введите фамилию и оценку: ")
    students.append(line)

# 1. Выводим всех
for student in students:
    print(student)

# 2. Выводим пустую строку
print()

# 3. Выводим только отличников и хорошистов
for student in students:
    # Разделяем строку по пробелу: ["Иванов", "5"]
    parts = student.split()
    # Оценка — это второй элемент (индекс 1)
    grade = int(parts[1])
    
    if grade == 4 or grade == 5:
        print(student)