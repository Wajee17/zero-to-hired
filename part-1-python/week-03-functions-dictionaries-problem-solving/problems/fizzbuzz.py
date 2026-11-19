def fizzbuzz(n):
    """Return "FizzBuzz" if n is divisible by 3 and 5, "Fizz" if by 3, "Buzz" if by 5, else str(n)."""
    is_number = isinstance(n, int) and not isinstance(n, bool)
    if not is_number:
        raise TypeError ("The entered value should be a number")
    elif n < 1:
        raise ValueError ("Number should not be less than 1")

    if n % 3 == 0 and n % 5 == 0:
        result = "FizzBuzz"
    elif n % 3 == 0:
        result = "Fizz"
    elif n % 5 == 0:
        result = "Buzz"
    else:
        result = str(n)

    return result

assert fizzbuzz(15) == "FizzBuzz"
assert fizzbuzz(30) == "FizzBuzz"
assert fizzbuzz(6) == "Fizz"
assert fizzbuzz(10) == "Buzz"
assert fizzbuzz(1) == '1'
assert fizzbuzz(7) == '7'
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(5) == 'Buzz'
print("all tests passed")

print(fizzbuzz(0))


