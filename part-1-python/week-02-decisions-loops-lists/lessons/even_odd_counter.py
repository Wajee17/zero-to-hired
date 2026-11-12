numbers = input("Numbers: ")

nums = numbers.split()

evens = 0
for num in nums:
    if int(num) % 2 == 0:
        evens += 1
print(f"Even: {evens}, Odd: {len(nums) - evens}")

