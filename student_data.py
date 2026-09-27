# student_data.py
# stores student details.

# Roll number is used as the key.
# name and marks are stored for each student.
students = {}


def add_student():
    roll = input("Enter roll number: ")
    if roll in students:
        print("roll number already exists.\n")
        return
    name = input("Enter student name: ")
    students[roll] = {"name": name, "marks": []}
    print("Student added.\n")


def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted.\n")
    else:
        print("No student found with that roll number.\n")




