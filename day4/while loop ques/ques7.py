# Count digits of a number
digit = int (input("enter a number to count digits : "))
count = 0
while digit > 0:
    digit = digit // 10
    count += 1
print("Number of digits:", count)