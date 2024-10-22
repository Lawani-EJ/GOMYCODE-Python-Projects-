![ProjectTask](/assets/CompletedCheckpointScreenshots/Screenshot%20(122).png)

# Student Marks and Grade Calculator

## Overview

This Python program allows users to input the marks of multiple students across various subjects and calculates each student's total marks, percentage, and final grade based on their performance. It utilizes NumPy for efficient data management and calculations, making the process of handling student marks smooth and fast.

## Features

- Handles multiple students and multiple subjects.
- Accepts and stores marks for each subject entered by the user.
- Automatically calculates the total marks and percentage for each student.
- Assigns grades based on predefined percentage ranges:
  - A+ for 90% and above
  - A for 80% to 89%
  - B+ for 70% to 79%
  - B for 60% to 69%
  - C for 50% to 59%
  - F for below 50%
- Displays a detailed summary of each student’s total marks, percentage, and grade.

## How It Works

1. **Input:** The user provides:
   - The number of students.
   - The number of subjects each student is enrolled in.
   - The marks obtained by each student in each subject.

2. **Data Storage:** The marks are stored in a NumPy array for efficient data handling and manipulation.

3. **Total Calculation:** The program calculates the total marks for each student by summing up the marks of all subjects.

4. **Percentage Calculation:** The percentage for each student is calculated by dividing their total marks by the maximum possible marks (number of subjects multiplied by 100).

5. **Grading:** Based on the calculated percentage, the program assigns a grade to each student according to the following ranges:
   - **A+:** 90% and above
   - **A:** 80% to 89%
   - **B+:** 70% to 79%
   - **B:** 60% to 69%
   - **C:** 50% to 59%
   - **F:** Below 50%

6. **Output:** The program displays a summary table that includes:
   - The student number.
   - Total marks obtained.
   - Percentage.
   - Grade.

## How It Was Built

The program was built using the following Python features:
- **NumPy:** To handle the multi-dimensional array that stores students' marks and perform operations like summation and percentage calculation.
- **Loops:** For gathering input and calculating the necessary totals and percentages.
- **Conditional Statements:** To determine the appropriate grade based on the calculated percentage.