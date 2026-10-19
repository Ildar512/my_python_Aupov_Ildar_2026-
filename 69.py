m = int(input("Сколько блюд в меню? "))
all_dishes = set()

for i in range(m):
    all_dishes.add(input("Доступное блюдо: "))

n = int(input("Сколько дней? "))
cooked_dishes = set()

for day in range(n):
    # Считываем строку и сразу разбиваем её на отдельные блюда по пробелам
    daily_menu = input(f"Блюда за день {day + 1}: ").split()
    
    # Добавляем все блюда этого дня в общий список приготовленного
    for dish in daily_menu:
        cooked_dishes.add(dish)

# Вычисляем разность множеств: блюда, которые есть в меню, но не были приготовлены
never_cooked = all_dishes - cooked_dishes

# Выводим результат
for dish in never_cooked:
    print(dish)