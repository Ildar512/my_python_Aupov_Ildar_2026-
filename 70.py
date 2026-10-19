line1 = input("Введите первое множество: ").split()
line2 = input("Введите второе множество: ").split()

result = []

# 1. Ищем элементы, которые есть в первом, но нет во втором
for num in line1:
    if num not in line2 and num not in result:
        result.append(num)

# 2. Ищем элементы, которые есть во втором, но нет в первом
for num in line2:
    if num not in line1 and num not in result:
        result.append(num)

if result:
    print(" ".join(result))
else:
    print("EMPTY")