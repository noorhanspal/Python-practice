def sum (x,y):
  return (x+y)
def sub (x,y):
  return (x-y)
def mul (x,y):
  return (x*y)
def div (x,y):
  return (x/y)

while True :
  print("Press 1 to ADD")
  print("Press 2 to SUB")
  print("Press 3 to MUL")
  print("Press 4 to DIV")
  print("Press 5 to EXIT")

  choice = int(input("Enter your choice (1 to 5): "))
  if choice == 5:
    print("Exit the program")
    break

  elif choice in (1,2,3,4):
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    if choice == 1:
      print(f"{num1} + {num2} = {(sum(num1,num2))}")

    elif choice == 2:
      print(f"{num1} - {num2} = {(sub(num1,num2))}")

    elif choice == 3:
      print(f"{num1} * {num2} = {(mul(num1,num2))}")

    elif choice == 4:
      if num2!=0:
        print(f"{num1} / {num2} = {(div(num1,num2))}")
      else:
        print("can't divide by zero")

    else:
      print("invalid choice")

    cal = input(" you want further calculation type(yes/no): ")
    if cal == 'No' or cal == 'no' or cal == 'NO' or cal=='nO':
      print("Program Ended")
      break

  else:
    print("Invalid choice")