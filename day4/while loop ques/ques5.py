# Find factorial of a number
num = int(input("enter a number to find factorial : "))
fact = 1
i = 1
while(i<=num):
  fact = i*fact
  i = i+1
print(fact)