# Check whether a number is prime
number = int(input("Enter a number: "))
is_prime = True
if number <= 1:
    is_prime = False
else:
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")