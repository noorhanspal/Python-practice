students = {
    "Noor": 85,
    "Simran": 92,
    "Karan": 78,
    "Aman": 95
}

highest = 0
top_student = ""

for name in students:
    if students[name] > highest:
        highest = students[name]
        top_student = name

print("Highest marks:", highest)
print("Student:", top_student)