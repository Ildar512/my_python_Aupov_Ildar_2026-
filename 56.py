total = 0
count = 0
found_at = -1

while True:
    n = int(input("Введите число: "))
    if n == 0:
        break
        
    count += 1
    total += n
    
    if total == 10 and found_at == -1:
        found_at = count

print(found_at)