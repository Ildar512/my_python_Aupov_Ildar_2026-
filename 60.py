total = 0
count = 0

while True:
    n = int(input("Введите число: "))
    
    if n == 0:
        print("ОК")
        break
        
    total += n
    count += 1
    
    if total > 100:
        print("СТОП")
        print(count)
        break