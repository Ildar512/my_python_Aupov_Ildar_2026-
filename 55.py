a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))

for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

print()  # перенос строки в конце