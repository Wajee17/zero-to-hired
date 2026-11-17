

def is_even(n):
    """Return True if n is even, otherwise False.

    Args:
        n (int): The number to check. Zero and negative numbers are allowed.

    Returns:
        bool: True if n is divisible by 2, False otherwise.

    Examples:
        >>> is_even(4)
        True
        >>> is_even(-3)
        False
    """
    if n % 2 == 0:
        return True
    else:
        return False

def gcd(a, b):
    """Return the greatest common divisor of a and b.

    Checks every number from 1 up to the smaller of a and b and keeps
    the largest one that divides both. If one input is 0, the other
    input is returned, since every number divides 0.

    Args:
        a (int): A non-negative integer.
        b (int): A non-negative integer.

    Returns:
        int: The largest integer that divides both a and b.

    Examples:
        >>> gcd(12, 18)
        6
        >>> gcd(17, 5)
        1
        >>> gcd(0, 9)
        9
    """
    gcd = max(a, b)
    for n in range(1, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            gcd = n
    return gcd

def word_stats(text):
    """Count the words in text and find the longest one.

    Words are split on any whitespace, so extra spaces are ignored.

    Args:
        text (str): The text to analyze.

    Returns:
        tuple: (word_count, longest_word). If several words tie for the
        longest, the first one is returned. If text has no words,
        returns (0, None).

    Examples:
        >>> word_stats("  the quick  brown fox ")
        (4, 'quick')
        >>> word_stats("   ")
        (0, None)
    """
    words = text.split()
    if not words:
        return 0, None
    return len(words), max(words, key=len)




print(is_even(4))
print(is_even(7))
print(is_even(0))
print(is_even(-3))

print(gcd(12,18))
print(gcd(17,5))
print(gcd(10,10))
print(gcd(0,9))

print(word_stats("  the quick  brown fox "))
print(word_stats("hi"))
print(word_stats("   "))
print(word_stats("ab cd ef"))
    
