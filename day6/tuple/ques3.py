# Create a tuple containing duplicate numbers and write a program to count how many times a particular number occurs.
numbers = (1,2,3,4,5,6,7,8,9,1,2,3,4,5)
num = int(input("Enter number you want to count : "))
if num in numbers:
  count = numbers.count(num)
  print("number occur ",count," times")
else:
  print("Number not found")