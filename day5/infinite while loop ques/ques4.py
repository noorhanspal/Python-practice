# Write a Python program using while True to take numbers from the user and count how many are positive, negative, and zero. Stop when the user enters 0.
positive = 0
negative = 0
zero = 0
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    elif num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print(f"Count of positive numbers: {positive}")
print(f"Count of negative numbers: {negative}")
print(f"Count of zeros: {zero}")