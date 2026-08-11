#Find sum of digits of a number
digit = int (input("enter a number  : "))
sum = 0
while digit > 0:
  sum = sum + digit%10
  digit = digit//10
print("sum of digits is : ",sum)