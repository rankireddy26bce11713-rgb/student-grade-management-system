# display.py
# Handles showing student records on screen.

from student_data import students
from marks_operations import calculate_average, calculate_grade


def view_student():
    roll = input("Enter roll number: ")
    if roll not in students:
        print("No student found with that roll number.\n")
        return
    info = students[roll]
    marks = info["marks"]
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    print("\nRoll No :", roll)
    print("Name    :", info["name"])
    print("Marks   :", marks)
    print("Average :", avg)
    print("Grade   :", grade)
    print()


def view_all_students():
    if len(students) == 0:
        print("No students added yet.\n")
        return
    print("\nRoll No | Name | Average | Grade")
    print("-" * 35)
    for roll in students:
        info = students[roll]
        avg = calculate_average(info["marks"])
        grade = calculate_grade(avg)
        print(roll, "|", info["name"], "|", avg, "|", grade)
    print()





