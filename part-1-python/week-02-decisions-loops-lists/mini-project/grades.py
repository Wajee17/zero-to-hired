import sys
scores = []
grades = []
while True:
    score = input("Score: ").strip()
    if not score:
        break
    if not score.isdigit():
        print("Not a whole number")
        continue
    elif not 0 <= int(score) <= 100:
        print("Out of range: scores go from 0 to 100")
        continue
    scores.append(int(score))
 
if not scores:
    print("No grades entered")
    sys.exit()

total = 0
highest = scores[0]
lowest = scores[0]
for score in scores:
    total += score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    if score >= 90:
        grades.append('A')
    elif score >= 80:
        grades.append('B')
    elif score >= 70:
        grades.append('C')
    elif score >= 60:
        grades.append('D')
    else:
        grades.append('F')

graded_scores = ", ".join(f"{score} ({grade})" for score, grade in zip(scores, grades))
avg = total / len(scores)
if avg >= 90:
    avg_grade = 'A'
elif avg >= 80:
    avg_grade = 'B'
elif avg >= 70:
    avg_grade = 'C'
elif avg >= 60:
    avg_grade = 'D'
else:
    avg_grade = 'F'



print(f"Scores: {graded_scores}")
print(f"Count: {len(scores)}")
print(f"Average: {avg:.1f} ({avg_grade})")
print(f"Highest: {highest}  Lowest: {lowest}")
print(f"A: {grades.count('A')}  B: {grades.count('B')}  C: {grades.count('C')}  D: {grades.count('D')}  F: {grades.count('F')}")





    


    