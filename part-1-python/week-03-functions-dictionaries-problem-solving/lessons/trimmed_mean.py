def trimmed_mean(nums):
    """Input: list of numbers. Minimum size of list = 3
    Output: trimmed average of the list (float)
    Raises:
        TypeError: if any element is not a number (bools are rejected)
        ValueError: if the list has fewer than 3 elements"""
    is_all_numbers = all(isinstance(num, (int, float)) and not isinstance(num, bool) for num in nums)
    if not is_all_numbers:
        raise TypeError ("Input should be a list of numbers")
    if len(nums) < 3:
        raise ValueError ("Input list should have at least 3 elements")
    
    trimmed_nums = nums[:]
    trimmed_nums.remove(max(nums))
    trimmed_nums.remove(min(nums))
    return sum(trimmed_nums) / len(trimmed_nums)

assert trimmed_mean([1, 2, 3, 4, 5, 6]) == 3.5
assert trimmed_mean([1, 1, 2, 3, 4]) == 2.0
assert trimmed_mean([-1, 3, 4, -4]) == 1.0
assert trimmed_mean([3, 3, 3]) == 3.0
assert trimmed_mean([1.5, 2.5, 3.5, 10.0]) == 3.0

check_list = [1, 2, 3, 4, 5]
trimmed_mean(check_list)
assert check_list == [1, 2, 3, 4, 5]
print("all tests passed")
trimmed_mean([5, 7])
trimmed_mean(["a", 1, 2])