total_bill = int(input("Total bill: "))
total_people = int(input("People: "))
print("Each pays:", total_bill // total_people)
print("Left over:", total_bill % total_people)