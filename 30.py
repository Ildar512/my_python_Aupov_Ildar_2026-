a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("ОШИБКА")
    else:
        print(a / b)
else:
    print("ОШИБКА")