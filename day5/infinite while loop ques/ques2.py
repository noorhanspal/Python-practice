# Write a Python program using while True to take numbers from the user and find the second largest number. Stop when the user enters -1.
largest = 0
while True:
    num = float(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    else:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
print(f"The second largest number is: {second_largest}")