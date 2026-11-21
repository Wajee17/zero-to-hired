def owners(phonebook, number):
    """Return the names in phonebook whose number exactly matches number, or [] if none."""
    result = []
    for name, num in phonebook.items():
        if num == number:
            result.append(name)
    return result


book = {"Ali": "0300-111", "Sara": "0321-222", "Omar": "0300-111"}


assert owners(book, '0300-111') == ['Ali', 'Omar']
assert owners(book, '0321-222') == ['Sara']
assert owners(book, '0300') == [] 
assert owners({}, '0300-111') == []
assert owners(book, '') == []
assert owners(book, 9) == []

print("all tests passed")