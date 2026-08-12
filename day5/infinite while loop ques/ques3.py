# Write a Python program using while True to take a number from the user and print its reverse. Ask the user whether they want to continue.
while True:
    reverse = 0
    num = int(input("Enter a number to reverse : "))
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    print(f"The reverse of the number is: {reverse}")
    choice = input("Do you want to continue? (yes/no): ")
    if choice == 'no':
        break
    