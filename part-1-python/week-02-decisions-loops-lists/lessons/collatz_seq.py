import sys

num = int(input("Start: "))

if num < 1:
    print("Start must be 1 or more")
    sys.exit()

steps = 0
chain = str(num)
while num > 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
        
    chain += f" -> {num}"
    steps += 1

print(chain)
print(f"Steps: {steps}")