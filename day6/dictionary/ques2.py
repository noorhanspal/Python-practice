# Create a dictionary of employee names and salaries. Write a program to search for an employee and display their salary.
employees = {
  "John": 50000,
  "Jane": 60000,
  "Mike": 55000,
  "Emily": 70000,
  "David": 65000
}   

employee_name = input("Enter the name of the employee: ")
if employee_name in employees:
    print(f"Salary of {employee_name}: ${employees[employee_name]}")
else:
    print("Employee not found.")