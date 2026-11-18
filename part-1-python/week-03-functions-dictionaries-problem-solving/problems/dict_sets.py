def letter_freq(text):
    """Return a dictionary mapping each lowercase alphabetic character in text to its frequency."""
    counter = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            counter[letter] = counter.get(letter, 0) + 1
    return counter

print(letter_freq("Hello, World!"))
print(letter_freq(""))
print(letter_freq("AAa"))


def common(a, b):
    """Return a sorted list of unique elements present in both iterables a and b."""
    set_a, set_b = set(a), set(b)
    common_set = set_a & set_b
    return list(sorted(common_set))

print(common([1, 2, 2, 3], [2, 3, 4]))
print(common([], [1]))
print(common(["y", "x"], ["x", "y", "x"]))


def two_sum_slow(numbers_list, target):
    """Return the indices of the first two numbers in numbers_list that add up to target using brute force."""
    for i in range(len(numbers_list)):
        for j in range(i+1, len(numbers_list)):
            if numbers_list[i] + numbers_list[j] == target:
                return i, j
       
print(two_sum_slow([2, 7, 11, 15], 9))
print(two_sum_slow([3, 2, 4], 6))
print(two_sum_slow([3, 3], 6))
print(two_sum_slow([1, 2], 10))


def two_sum(number_list, target):
    """Return the indices of the two numbers in number_list that add up to target using a hash map."""
    seen = {}
    j = 0
    for num in number_list:
        if (target - num) in seen:
            return seen[target - num], j
        seen[num] = j
        j += 1
    
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2], 10))