phone = {"Ali": "0300-111", "Sara": "0321-222"}
print(phone["Sara"])

phone["Omar"] = "0333-333"
phone["Ali"] = "0300-999"
print(len(phone), "Ali" in phone, "0321-222" in phone)
print(phone)

print(phone.get("Zoe"), phone.get("Zoe", "unknown"))
print(phone["Zoe"])