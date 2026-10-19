word = input("Введите сообщение: ")
n = int(input("Введите номер буквы: "))

if 1 <= n <= len(word):
    # В Python индексация с нуля, поэтому вычитаем 1
    print(word[n - 1])
else:
    print("ОШИБКА")