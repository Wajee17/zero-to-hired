def second_largest(nums):
    """Return the second largest unique number in nums, or None if all values are equal.

    Raises ValueError if nums is empty and TypeError if it contains non-numeric values.
    """
    set_nums = set(nums)
    is_number = all(isinstance(n, int) and not isinstance(n, bool) for n in set_nums)
    if not set_nums:
        raise ValueError ("Input list was empty")
    elif not is_number:
        raise TypeError ("The values of entered list should be a number")
    elif len(set_nums) == 1:
        return None

    sorted_set = sorted(set_nums)
    return sorted_set[-2]


assert second_largest([9, 9, 7]) == 7
assert second_largest([9, 9, 7, 9, 9, 7, 7, 4, 9]) == 7
assert second_largest([9, 9, 10]) == 9
assert second_largest([-9, -9, -7, -20]) == -9
assert second_largest([9, 9]) is None
assert second_largest([9, 9, 9, 9, 9, 9]) is None
assert second_largest([9, 3]) == 3


print("all tests passed")

print(second_largest([]))