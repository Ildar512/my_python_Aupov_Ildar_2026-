answer1 = input("Ты сегодня выспался? (да/нет): ")
answer2 = input("Ты сегодня ел? (да/нет): ")

if answer1 == "да" and answer2 == "да":
    print("Ты готов свернуть горы! ")
elif answer1 == "да" and answer2 == "нет":
    print("Энергия есть, но желудок пуст. Поешь! ")
elif answer1 == "нет" and answer2 == "да":
    print("Сытый, но сонный. Кофе в помощь ")
else:
    print("Тебе нужен отдых и обед. ")