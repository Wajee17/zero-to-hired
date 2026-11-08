item = input("Item: ").lower()
price = float(input("Price: "))
quantity = int(input("Quantity: "))

code = f"{item[0:3].upper()}-{quantity}"
total = price * quantity

print(f"Code: {code}")
print(f"Total: {total}")
