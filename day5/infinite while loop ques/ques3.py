# Write a Python program using while True to take a number from the user and print its reverse. Ask the user whether they want to continue. Stop when the user enters no.
while True:
    num = input("Enter a number: ")
    reversed_num = num[::-1]
    print(f"The reverse of {num} is {reversed_num}")
    
    cont = input("Do you want to continue? (yes/no): ").strip().lower()
    if cont == 'no':
        break