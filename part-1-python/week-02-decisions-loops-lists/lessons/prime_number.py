import sys

num = int(input("Number: "))
if num < 2:
    print(f"{num} is not prime")
    sys.exit()

for divisor in range(2, num):
    if num % divisor == 0:
        print(f"{num} is not prime (divisible by {divisor})")
        break
else:
    print(f"{num} is prime")