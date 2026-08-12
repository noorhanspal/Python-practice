# Write a Python program using while True to continuously take numbers from the user and calculate the sum and average. Stop when the user enters 0.
total = 0
count = 0
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    average = total / count
    print(f"The sum is: {total}")
    print(f"The average is: {average}")
else:
    print("No numbers were entered.")