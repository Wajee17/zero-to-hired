word = input("Word: ")

reverse = word[-1::-1]
middle = word[len(word) // 2]

print(f"Reversed: {reverse}")
print(f"Middle: {middle}")