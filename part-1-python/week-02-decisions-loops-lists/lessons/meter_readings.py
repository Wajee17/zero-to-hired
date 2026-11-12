import sys

houses = int(input("Houses: "))

if houses < 1:
    print("No readings")
    sys.exit()

readings = []


for num in range(houses):
    reading = float( input(f"Reading {num + 1}: "))
    readings.append(reading)


total = 0
highest_reading = readings[0]
highest_house = 1

for house_num, reading in enumerate(readings, start= 1):
    total += reading
    if reading > highest_reading:
        highest_reading = reading
        highest_house = house_num

avg = total / houses


print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Highest: {highest_reading} (house {highest_house})")
