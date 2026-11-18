def letter_grade(score):
    """Return 'A' for 90+, 'B' for 80+, 'C' for 70+, 'D' for 60+, else 'F'.
    Raises ValueError if scores is outside 0-100"""
    if not 0 <= score <= 100:
        raise ValueError(f"score must be 0–100, got {score}") 
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def group_by_grade(scores):
    """input: dictionary of key = name : value = score
    output: dictionary of key = 'grade': value = list of names"""
    grade_names = {}
    for name, score in scores.items():
        grade = letter_grade(score)
        if grade not in grade_names:
            grade_names[grade] = []
        grade_names[grade].append(name)
    return grade_names

students = {"Ali": 91, "Sara": 78, "Omar": 85, "Zoe": 95, "Hamza": 58}
print(group_by_grade(students))
print(group_by_grade({}))
