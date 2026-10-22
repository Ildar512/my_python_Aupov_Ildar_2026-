# Считываем белый список до пустой строки
whitelist = set()
while True:
    text = input("Белый список (Enter для завершения): ")
    if text == "":
        break
    whitelist.add(text)

# Считываем запросы до пустой строки
queries = []
while True:
    text = input("Запрос (Enter для завершения): ")
    if text == "":
        break
    queries.append(text)

# Выводим только те запросы, которые есть в белом списке
for query in queries:
    if query in whitelist:
        print(query)