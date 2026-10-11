secret = 42

while True:
    guess = int(input("Угадайте число: "))

    if guess < secret:
        print("БОЛЬШЕ")
    elif guess > secret:
        print("МЕНЬШЕ")
    else:
        print("УГАДАЛ!")
        break