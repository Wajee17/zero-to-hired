def letter_grade(score):
    """Return 'A' for 90+, 'B' for 80+, 'C' for 70+, 'D' for 60+, else 'F'.
    Raises ValueError if scores is outside 1-100"""
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
            
    

def class_report(scores):
    """Return (average, average_letter, letters) for a list of scores.
    Must use letter_grade. Must not change the list it's given. Raises ValueError if scores is empty."""

    if not scores:
        raise ValueError("class_report needs at least one score")
    average = sum(scores)/ len(scores)
    average_letter = letter_grade(average)
    letters = [letter_grade(score) for score in scores]
    return (average, average_letter, letters)

print(letter_grade(90), letter_grade(89.95), letter_grade(0))
avg, letter, letters = class_report([95, 82, 67, 88, 45])
print(avg, letter, letters)
print(letter_grade(-5))