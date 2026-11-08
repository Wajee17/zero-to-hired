dist_in_km = float(input("Kilometres: "))
wt_in_kg = float(input("Kilograms: "))
duration_in_mins = int(float(input("Minutes: ")))

print(f"{dist_in_km} km = {dist_in_km * 0.621371} miles")
print(f"{wt_in_kg} kg = {wt_in_kg * 2.20462} lbs")
print(f"{duration_in_mins} min = {duration_in_mins // 60} h {duration_in_mins % 60} min")

