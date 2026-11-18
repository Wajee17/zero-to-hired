words = "the cat and the hat and the bat".split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)

for word, n in counts.items():
    if n > 1:
        print(word, n)
        