def add_bonus(scores):
    scores.append(100)

def reset(scores):
    scores.clear()

def reset(scores):
    scores[:] = []

def shout(word):
    word = word.upper()

marks = [70, 80]
add_bonus(marks)
print(marks)
reset(marks)
print(marks)

name = "ada"
shout(name)
print(name)