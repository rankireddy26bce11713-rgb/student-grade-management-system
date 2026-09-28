# Project Statement: Student Grade Management System

## Problem Statement
teachers and school administrators need a straight forward way to record student scores and calculate final grades without relying to tedious manual calculations or overly complicated spreadsheets. this project offers a simple, command-line tool that lets users track students, double check score entries, and generate grades automatically-saving time and reducing errors.

## Scope of the Project
This project is a lightweight, offline python application that manages student data in memory using standard CRUD(Create, Read, Update, Delete) features. It tracks basic student details-such as roll numbers and names-along with their numerical marks. The program uses clear,  modular code to calculate averages and assign letter grades on demand. Because data persistence (like saving to a database or text file) is out of scope for this version, all stored information resets once the program closes.

## Target Audience
* **Teachers** Looking for a quick way to handle daily class records and grade calculations.
* **School Administrative Staff** Handling student enrolment and managing overall grade entries.
* **Teaching Assistants** Needing a simple tool to calculate assignment and quiz averages quickly.

## key Features
* **Secure Student Registration:** Checks roll numbers upon registration to make sure no two students have the same ID
* **Automated Data Processing:** Compute overall student averages on the fly as marks are entered.
* **letter Grading System:** maps final score averages to standard letter grades (S to F) using clear grading thresholds.
* **Organized Code Base:** Split cleanly across five distinct python scrips to separate the user interface, storage, and calculation logic.
* **Input Validation:** Blocks invalid entries-like negative numbers or scores over 100-and handles unexpected user errors smoothly.
