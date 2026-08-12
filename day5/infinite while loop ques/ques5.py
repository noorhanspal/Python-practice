# 5. Write a Python program using while True to create a number guessing game. The user keeps entering numbers until they guess the correct number. After a correct guess, display the number of attempts.
while True:
    import random
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thank you for playing! Goodbye!")
        break