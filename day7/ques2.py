# create list in which add,update,remove,display students with the help of function
students = []

# Add student
def add():
  name = input("Enter student Name : ")
  roll = input("Enter student roll no : ")
  students.append([name,roll])
  print("Student Added Successfully ")

# Display students 
def display():
  if len(students)!=0:
    for student in students :
      print(student)
  else:
    print("No Student Found")

# remove students
def remove ():
  name = input("enter name you want to remove : ")
  for student in students:
    if student[0]==name:
      students.remove(student)
      print("Student removed")
      return
    else:
      print("no student found")

#  update 
def update ():
  roll = input("Enter roll no you want to update : ")
  for student in students:
    if roll == student[1]:
      new= input("enter new name : ")
      student[0]=new
      print("student updated")
      return
  print("No student found")

while True:
  print("press 1 to add student")
  print("press 2 to display student")
  print("press 3 to remove studen(t")
  print("press 4 to update student")
  print("press 5 to exit")

  choice = int(input("enter your choice : "))
  if choice == 1:
    add()
  elif choice == 2:
    display()
  elif choice == 3:
    remove()
  elif choice == 4:
    update()
  elif choice == 5:
    print("exit")
    break
  else:
    print("invalid choice")
