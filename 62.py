n = int(input("Сколько городов будет введено? "))

cities = set()

for i in range(n):
    city = input("Введите город: ")
    cities.add(city)

new_city = input("Введите новый город для проверки: ")

if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK")