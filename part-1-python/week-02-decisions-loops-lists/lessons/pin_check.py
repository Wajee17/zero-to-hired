user_pin = "4721"
max_tries = 3
for attempt in range(max_tries):
    pin = input("PIN: ")
    if pin == user_pin:
        print("Access granted.")
        break
    else:
        attempts_left = max_tries - 1 - attempt
        if attempts_left > 0:
            print(f"Wrong PIN. {attempts_left} {'attempts left' if attempts_left > 1 else 'attempt left'}.")

else:
    print("Card blocked.")