m = int(input("Сколько продуктов в холодильнике? "))
fridge = set()

for i in range(m):
    fridge.add(input("Продукт: "))

n = int(input("Сколько рецептов? "))

for i in range(n):
    # Считываем строку рецепта целиком и разделяем её по пробелам
    recipe_line = input("Рецепт и ингредиенты: ").split()
    
    # Первое слово — это название рецепта, остальные — ингредиенты
    recipe_name = recipe_line[0]
    ingredients = recipe_line[1:]
    
    # Проверяем: если ВСЕ ингредиенты есть в холодильнике
    can_cook = True
    for item in ingredients:
        if item not in fridge:
            can_cook = False
            break  # Если хотя бы одного нет, дальше проверять нет смысла
            
    if can_cook:
        print(recipe_name)