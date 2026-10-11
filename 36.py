while True:
    password = input("Введите пароль: ")
    confirm = input("Повторите пароль: ")

    if len(password) < 8:
        print("Слишком короткий!")
    elif "123" in password:
        print("Содержит 123!")
    elif password != confirm:
        print("Пароли не совпадают!")
    else:
        print("OK")
        break