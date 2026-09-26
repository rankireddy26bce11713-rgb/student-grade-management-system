# Project Statement: Student Grade Management System

## Problem Statement
Educators and school administrators frequently need a centralized, lightweight tool to process student scores and calculate academic grades. Manual calculation is prone to errors, and complex spreadsheet software can be unnecessarily bloated for simple administrative tasks. This project provides an automated, terminal-based solution to track students, validate inputted scores, and compute grades instantly, reducing administrative overhead and increasing accuracy.

## Scope of the Project
The scope of this project is limited to a local, text-based Python application executing CRUD (Create, Read, Update, Delete) operations in memory. It manages core student identifiers (roll number and name) alongside a dynamic list of numerical marks. The system utilizes modular logic to generate immediate averages and assign letter grades upon user request. Data persistence (saving to a file or database) is outside the current scope, meaning data is reset upon exiting the application.

## Target Users
* **Teachers** managing day-to-day class records and needing quick calculations.
* **School Administrative Staff** processing student onboarding and grading.
* **Teaching Assistants** requiring a fast, reliable tool to compute averages for assignments or quizzes.

## High-Level Features
* **Secure Student Registration:** Prevents duplicate student entries by enforcing unique roll numbers.
* **Automated Data Processing:** Calculates cumulative averages dynamically from an array of inputted marks.
* **Conditional Grading System:** Translates numerical averages into standard letter grades (A+ through F) using a predefined logical ladder.
* **Modular Architecture:** Separates data storage, user interface, and calculation logic across five specific Python modules for clean, maintainable code.
* **Input Validation:** Ensures data integrity by rejecting out-of-bound marks (e.g., negative numbers or values over 100) and handling invalid user inputs gracefully.
