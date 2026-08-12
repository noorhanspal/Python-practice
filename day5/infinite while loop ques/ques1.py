# Write a Python program using while True to continuously take numbers from the user and calculate the sum and average. Stop when the user enters 0.
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    else:
        total += num
        count += 1

if count > 0:
    average = total / count
    print(f"Sum: {total}")
    print(f"Average: {average}")
else:
    print("No numbers were entered.")