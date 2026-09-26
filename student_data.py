# student_data.py
# Handles the main student dictionary and basic add/delete operations.

# One dictionary holds every student.
# Roll number (a string) is the key.
# The value is another dictionary: {"name": ..., "marks": [list of numbers]}
students = {}


def add_student():
    roll = input("Enter roll number: ")
    if roll in students:
        print("A student with this roll number already exists.\n")
        return
    name = input("Enter student name: ")
    students[roll] = {"name": name, "marks": []}
    print("Student added successfully.\n")


def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted.\n")
    else:
        print("No student found with that roll number.\n")




