# Task 1: Student Marks Dictionary

# Dictionary containing student names and marks
student_marks = {
    "Shahrukh": 92,
    "Aman": 85,
    "Rahul": 78,
    "Priya": 88,
    "Neha": 95
}

# Ask user to enter student name
name = input("Enter the student's name: ")

# Display marks if student exists
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")