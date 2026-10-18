m = int(input("Сколько книг в библиотеке? "))
library = set()

for i in range(m):
    library.add(input("Введите название книги: "))

n = int(input("Сколько книг в летнем списке? "))
summer_list = []

for i in range(n):
    summer_list.append(input("Введите книгу из списка: "))

for book in summer_list:
    if book in library:
        print("YES")
    else:
        print("NO")