import random


while True:
    secret = random.randint(1, 100)
    for attempt in range(1,8):
        while True:
            num = input("Number: ").strip()
            if not num.isdigit():
                print("Please enter a whole number")
            elif not 1 <= int(num) <= 100:
                print("Pick a number between 1 and 100")
            else:
                num = int(num)
                break
        if num > secret:
            print("Too high")
        elif num < secret:
            print("Too low")
        else:
            if attempt == 1:
                print(f"Got it in {attempt} attempt!")
            else:
                print(f"Got it in {attempt} attempts!")
            break
    else: 
        print(f"Ran out of attempts. Number was {secret}")
    if input("Play again? (y/n) ").strip().lower() != 'y':
        break