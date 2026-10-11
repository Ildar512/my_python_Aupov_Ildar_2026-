n = int(input("Введите число: "))
n = abs(n)

total = 0
for digit in str(n):
    total += int(digit)

print(total)