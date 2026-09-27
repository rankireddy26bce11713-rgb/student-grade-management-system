#main.py
# The starting point of the program.
# Run this file: python main.py

from student_data import add_student, delete_student
from marks_operations import add_marks
from display import view_student, view_all_students
from menu import show_menu

running = True
while running:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_marks()
    elif choice == "3":
        view_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting the program.")
        running = False
    else:
        print("Invalid choice. Please enter a number from 1 to 6.\n")
