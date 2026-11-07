text = input("Text: ").lower()

words = text.split()
text = "".join(words)

print(f"Palindrome: {text == text[::-1]}")