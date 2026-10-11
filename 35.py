password = input("Введите пароль: ")
confirm = input("Повторите пароль: ")

if len(password) < 8:
    print("Слишком короткий!")
elif password != confirm:
    print("Пароли не совпадают!")
else:
    print("OK")