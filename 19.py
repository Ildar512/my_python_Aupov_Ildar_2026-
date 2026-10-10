login = input("Введите логин: ")
email = input("Введите email: ")

if "@" in email and "@" not in login:
    print("OK")
else:
    print("ОШИБКА")