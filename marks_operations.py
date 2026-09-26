#marks_operations.py
# Handles adding marks and calculating averages/grades.

from student_data import students

def add_marks():
    roll = input("Enter roll number: ")
    if roll not in students:
        print("No student found with that roll number.\n")
        return
    mark = int(input("Enter marks (0-100): "))
    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.\n")
        return
    students[roll]["marks"].append(mark)
    print("Marks added.\n")


def calculate_average(marks_list):
    # Basic average: sum divided by count.
    if len(marks_list) == 0:
        return 0
    total = 0
    for m in marks_list:
        total = total + m
    return total / len(marks_list)


def calculate_grade(average):

# Simple if-elif-else ladder, same idea as Unit 3 conditionals.
    if average >= 90:
       grade = "S"
    elif average >= 80:
       grade = "A"
    elif average >= 70:
       grade = "B"
    elif average >= 60:
       grade = "C"
    elif average >= 50:
       grade = "D"
    else:
       grade = "F"
    return grade 



