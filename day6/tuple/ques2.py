# 2. Create a tuple of student names and write a program to search whether a given name exists in the tuple
student = ("noor","nav","roobal")
name = input("Enter name you want to search : ")
if name in student:
  index = student.index(name)
  print("Student Found at index : ",index)
else:
  print("student not found")