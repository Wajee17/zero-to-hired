first_name = input("First name: ")
last_name = input("Last name: ")

initials = f"{first_name[0]}.{last_name[0]}."
username = f"{first_name[:3].lower()}{last_name[:3].lower()}"
letters = len(first_name + last_name)

print(f"Initials: {initials}")
print(f"Username: {username}")
print(f"Letters: {letters}")