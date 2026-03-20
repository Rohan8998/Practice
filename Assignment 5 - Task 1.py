# Assignment 5: Task 1 - Student Marks Dictionary
# Module 6: Data Structures and Strings in Python

# Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Eve": 95,
    "Frank": 82
}

# Display all students and their marks
print("Student Marks Dictionary:")
print("-" * 40)
for name, marks in student_marks.items():
    print(f"{name}: {marks}")
print("-" * 40)

# Ask user to input a student's name
student_name = input("\nEnter a student's name to look up their marks: ").strip()

# Check if student exists and display marks or appropriate message
if student_name in student_marks:
    marks = student_marks[student_name]
    print(f"\n✓ {student_name}'s marks: {marks}")
else:
    print(f"\n✗ Student '{student_name}' not found in the dictionary.")
    print("Please check the spelling and try again.")
