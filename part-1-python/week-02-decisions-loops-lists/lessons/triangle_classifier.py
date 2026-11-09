import sys

print("Please enter the lengths of the three sides of the triangle.")
side_1 = float(input("Side 1: "))
side_2 = float(input("Side 2: "))
side_3 = float(input("Side 3: "))

if (side_1 <= 0 or side_2 <= 0 or side_3 <= 0):
    print("Not a triangle")
    sys.exit()
if side_1 + side_2 <= side_3 or side_1 + side_3 <= side_2 or side_2 + side_3 <= side_1:
    print("Not a triangle")
    sys.exit()
    
if side_1 == side_2 == side_3:
    print("Equilateral")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("Isosceles")
else:
    print("Scalene")

    