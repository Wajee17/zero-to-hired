import sys

nums_str = input("Numbers: ")
if not nums_str:
    print("No second largest")
    sys.exit()



nums_lst = nums_str.split()

largest = int(nums_lst[0])
second_largest = None

for num in nums_lst:
    num = int(num)
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest == None or second_largest < num):
        second_largest = num

if second_largest is None:
    print("No second largest")
else:
    print(f"Second largest: {second_largest}")  