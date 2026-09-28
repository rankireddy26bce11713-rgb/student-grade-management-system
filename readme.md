# Student Grade Management System

**Overview**
This project is a modular, command-line-based Python application designed to manage student records, record their marks, and automatically calculate averages and grades. The application uses an interactive menu to guide the user through various data management tasks, fulfilling the requirements for the VITyarthi flipped course evaluation.

## Features
*   **Add New Student:** Registers a new student in the system using a unique roll number.
*   **Add Marks:** Appends marks (validated between 0 and 100) to an existing student's record.
*   **View Individual Record:** Retrieves and displays a single student's name, marks list, calculated average, and assigned grade.
*   **View All Students:** Displays a formatted tabular overview of all enrolled students alongside their averages and grades.
*   **Delete Student:** Removes a student's data entirely from the system using their roll number.
*   **Interactive Menu:** Provides a persistent terminal loop to continuously perform actions until the user chooses to exit.

## Technologies and Tools Used
*   **Python 3:** Core programming language.
*   **Data Structures:** Standard Python Dictionary structure for in-memory data storage and quick lookups ($O(1)$ time complexity).
*   **Architecture:** Modular design splitting logic across 5 distinct `.py` files.

## Steps to Install & Run the Project
1. Make sure you have python 3 installed on your machine.
2. Download or clone the repository containing all project files (`student_data.py`, `mark_operations.py`, `display.py`, `menu.py`, `main.py`) in the same folder.
3. Open a terminal or launch your command prompt or terminal and cd into that project folder.
4. Run the application using the following command: 
   ```bash
   python main.py
   ```

## Instructions for Testing
*   **Validation Testing:** Attempt to enter a mark outside the 0-100 range to verify the error handling triggers correctly.
*   **Duplicate Handling:** Try to add a student with a roll number that already exists to confirm the system prevents duplication.
*   **Missing Data Testing:** Search for or attempt to delete a roll number that does not exist to trigger the "No student found" validation message.
*   **Edge Case Testing (Zero Marks):** View a student who has been added but has no marks assigned yet to verify the system handles empty arrays gracefully (returns a 0 average rather than throwing a division by zero error).
