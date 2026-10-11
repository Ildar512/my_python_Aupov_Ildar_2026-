result = ""

while True:
    n = int(input("Введите число: "))
    if n == 0:
        break
    result = result + str(n) + " "

print(result.strip())