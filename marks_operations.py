#marks_operations.py
# functions for marks and grades.

from student_data import students

def add_marks():
    roll = input("Enter roll number: ")
    if roll not in students:
        print("No student found with that roll number.\n")
        return
    mark = int(input("Enter marks (0-100): "))
    if mark < 0 or mark > 100:
        print("invalid marks.\n")
        return
    students[roll]["marks"].append(mark)
    print("Marks added.\n")


def calculate_average(marks_list):
    # calculate average.
    if len(marks_list) == 0:
        return 0
    total = 0
    for m in marks_list:
        total = total + m
    return total / len(marks_list)


def calculate_grade(average):

# Simple if-elif-else ladder.
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



