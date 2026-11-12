import sys

steps = input("Daily steps: ")
steps_lst = steps.split()

if not steps_lst:
    print("No data")
    sys.exit()

goal = input("Goal: ")
if not goal:
    print("Invalid goal")
    sys.exit()
else:
    goal = int(goal)
steps_int = [int(step) for step in steps_lst]

total_days = len(steps_int)
days_passed = 0
streak = 0
streak_days = []

for step in steps_int:
    
    if step >= goal:
        days_passed += 1
        streak += 1
    else:
        streak = 0
    streak_days.append(streak)

max_streak = max(streak_days)
streak_end = streak_days.index(max_streak) + 1
streak_start = streak_end - max_streak + 1


print(f"Days met goal: {days_passed} of {total_days}")
if days_passed == 0:
    print("Longest streak: 0 days")
else:
    print(f"Longest streak: {max_streak} days (day {streak_start} to day {streak_end})")


