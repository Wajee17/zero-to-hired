age = int(float(input("Age: ")))
if age < 0:
    print("Invalid age")
    exit()
elif age <= 4:
    ticket = "Infant"
    price = 0
elif age <= 17:
    ticket = "Child"
    price = 300
elif age <= 59:
    ticket = "Adult"
    price = 600
else:
    ticket = "Senior"
    price = 400

member = input("Member (y/n): ").lower()
if member != 'y' and member != 'n':
    print("Invalid Membership")
    exit()

price = (price - (price // 10)) if member == 'y' else price


print(f"Ticket: {ticket}")
print(f"Price: {price}")