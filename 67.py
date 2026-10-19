n = int(input("Сколько сотрудников? "))

surnames = []

for i in range(n):
    surnames.append(input("Введите фамилию: "))

# Считаем, сколько раз встречается каждая фамилия
counts = {}
for name in surnames:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

# Считаем количество однофамильцев
total_duplicates = 0
for name, count in counts.items():
    if count > 1:
        total_duplicates += count

print(total_duplicates)