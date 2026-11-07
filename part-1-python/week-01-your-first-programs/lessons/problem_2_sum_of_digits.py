number = int(input("Number: "))
num_1 = number % 10
number = number // 10
num_2 = number % 10
number = number // 10
num_3 = number % 10
print("Sum of digits:", num_1 + num_2 + num_3)
