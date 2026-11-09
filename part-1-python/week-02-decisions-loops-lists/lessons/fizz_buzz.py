number = int(input("Number: "))
result = "FizzBuzz" if (number % 3 == 0 and number % 5 == 0) else "Buzz" if number % 5 == 0 else "Fizz" if number % 3 == 0  else number

print(result)