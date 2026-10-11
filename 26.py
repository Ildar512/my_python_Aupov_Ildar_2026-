text = input("Введите сообщение: ")
total_kopecks = len(text) * 40

rubles = total_kopecks // 100
kopecks = total_kopecks % 100

print(f"{rubles} р. {kopecks} коп.")