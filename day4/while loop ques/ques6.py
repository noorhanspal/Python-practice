# reverse a number
num = int(input("enter a number to reverse : "))
reverse = 0
while(num>0):
  digit = num%10
  reverse = reverse*10 + digit
  num = num//10
print("reverse of the number is : ",reverse)
