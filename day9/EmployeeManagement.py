# Create a Python program using class, object, constructor, inheritance, and user input. Create a base class Employee with employee ID, name, and salary. Create a derived class Manager with department and bonus. Take all details from the user and display the complete employee information including total salary.
class Employee:
  def __init__(self,id,name,salary):
    self.id = id
    self.name=name
    self.salary=salary
  def display(self):
    print("Employee Id: ",self.id)
    print("Employee Name: ",self.name)
    print("Employee Salary: ",self.salary)
class Manager(Employee):
  def __init__(self, id, name, salary,department,bonus):
    super().__init__(id, name, salary)
    self.department = department
    self.bonus = bonus
  def display(self):
    super().display()
    print("Department : ",self.department)
    print("Bonus: ",self.bonus)
    Total = self.salary+ self.bonus
    print("Total salary : ",Total)  
Id = input("Enter Employee Id : ")
Name = input("Enter Employee Name : ")
Salary = float(input("Enter Salary : "))
Department = input("Enter department : ")
Bonus = float(input("Enter Bonus: "))
manager = Manager(Id, Name, Salary, Department, Bonus)
manager.display()