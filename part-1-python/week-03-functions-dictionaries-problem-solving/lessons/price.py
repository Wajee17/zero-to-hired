def price(amount, tax=0.17, discount=0):
    return round(amount * (1 + tax) - discount, 2)

print(price(100))
print(price(100, 0.05))
print(price(100, discount=10))
print(price(discount=10, amount=50))
print(price(100, 0.1, 5, 2))