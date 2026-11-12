import sys

words_str = input("Words: ")

words_lst = words_str.split()

if not words_lst:
    print("No words were entered")
    sys.exit()

keep = []
seen = []

for word in words_lst:
    if word.lower() not in seen:
        keep.append(word)
        seen.append(word.lower())

keep_str = " ".join(keep)
  
print(keep_str)