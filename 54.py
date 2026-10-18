count = 0
first_cat = -1
total_cats = 0

while True:
    text = input("Введите строку: ")
    if text == "СТОП":
        break
        
    count += 1
    
    if "кот" in text or "Кот" in text:
        total_cats += 1
        if first_cat == -1:
            first_cat = count

print(total_cats)
print(first_cat)
