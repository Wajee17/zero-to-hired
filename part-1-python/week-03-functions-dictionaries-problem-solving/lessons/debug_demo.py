def average_positive(nums):
    """Return the average of the positive numbers in nums."""
    total = 0
    count = 0
    for n in nums:
        if n > 0:
            total += n
            count += 1
        print(total, count)
    return total / count


assert average_positive([2, 4, 6]) == 4.0
assert average_positive([2, -4, 6]) == 4.0
print("all tests passed")