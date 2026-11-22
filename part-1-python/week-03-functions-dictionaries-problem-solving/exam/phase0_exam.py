def count_evens(nums):
    """Return the number of even integers in nums."""
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

assert count_evens([]) == 0
assert count_evens([0]) == 1
assert count_evens([2, 3, 5, 6, 8]) == 3
assert count_evens([-2, -3, -5, -6, -8]) == 3
assert count_evens([2, 3]) == 1
print("all tests passed")


print(count_evens([1, 2, 3, 4]))   # → 2
print(count_evens([]))             # → 0


def longest_word(words):
    """Return the longest word in words (first one on ties); raise ValueError if empty."""
    if not words:
        raise ValueError ("Input was empty")
    return max(words, key = len)

assert longest_word(['wajee', 'wajee', 'hai']) == "wajee"
assert longest_word(['wajee', 'wajee', 'haider']) == "haider"
assert longest_word(['wajee']) == "wajee"
assert longest_word(['ab', 'cd', 'ef']) == "ab"
assert longest_word(['', '']) == ""
print("all tests passed")

print(longest_word(["hi", "hello", "hey"]))     # → "hello"
print(longest_word(["ab", "cd"])   )            # → "ab"
#print(longest_word([])   )                      # → ValueError




def group_by_length(words):
    """Return a dict mapping each word length to the list of words with that length."""
    lengths = {}
    for word in words:
        lengths[len(word)] = lengths.get(len(word), [])
        lengths[len(word)].append(word)
    return lengths

assert group_by_length([]) == {}
assert group_by_length(['ant', 'bee', 'wasp']) == {3: ['ant', 'bee'], 4: ['wasp']}
assert group_by_length(['hi', 'hi']) == {2: ['hi', 'hi']}
assert group_by_length(['', 'a']) == {0: [''], 1: ['a']}
print("all tests passed")

print(group_by_length(["ant", "bee", "wasp", "fly"]))
