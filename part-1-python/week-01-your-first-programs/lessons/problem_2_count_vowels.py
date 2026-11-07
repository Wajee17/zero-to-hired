text = input("Text: ").lower()

a = text.count("a")
e = text.count("e")
i = text.count("i")
o = text.count("o")
u = text.count("u")

print(f"Vowels: {a + e + i + o + u}")