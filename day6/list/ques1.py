# student management system 
student =[]
while True:
  print("---STUDENT MANAGEMENT SYSTEM---")
  print("Enter 1 to ADD STUDENT")
  print("Enter 2 to DISPLAY STUDENT")
  print("Enter 3 to REMOVE STUDENT")
  print("Enter 4 to UPDATE STUDENT")
  print("Enter 5 to SEARCH STUDENT")
  print("Enter 6 to EXIT")

  choice = int(input ("Enter your choice (1 to 6) : "))

  # Add student
  if choice ==1:
    num = int (input ("enter number of student you want to add :  "))
    for i in range (num):
      name = input("enter name : ")
      student.append(name)
    print("student added successfuly")

  # Display student
  elif choice ==2:
    if len(student)==0:
      print("no student found")
    else:
      print("---DISPLAY STUDENT---")
      for i in student:
        print(i)

  # Remove student
  elif choice == 3:
    if len(student)==0:
      print("No student found")
    else:
      name = input("Enter Name yo want to remove : ")
      student.remove(name)
      print("student remove successfully")

  # update student
  elif choice == 4:
    if len(student)==0:
      print("No student found")
    else:
      name = input("Enter name you want to update : ")
      if name in student:
        new_name = input("Enter new name : ")
        index= student.index(name)
        student[index]=new_name
        print("Name updated Successfully")
      else:
        print("Invalid Name")

  # Search student
  elif choice == 5:
    if len(student)==0:
      print("No student found")
    else:
      name = input("Enter name you want to search : ")
      if name in student:
        index= student.index(name)
        print("Student found at index : ",index)
      else:
        print("Invalid Name")

  # Exit
  elif choice == 6:
    print("EXIT PROGRAM")
    break

  else:
    print("Invalid choice")
