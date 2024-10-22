![Assigned Project Task](/assets/CompletedCheckpointScreenshots/Screenshot%20(117).png)


# Calculator Application

## Overview
This is a simple command-line calculator application that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The calculator prompts the user to input two numbers and an operator, then computes and returns the result of the operation. 

## Features

- Supports the four basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  
- Handles division by zero by providing an appropriate error message and avoiding the invalid operation.

## How It Works

1. **Input:** The calculator takes three inputs from the user:
   - The first number (an integer)
   - The second number (an integer)
   - The arithmetic operator (`+`, `-`, `*`, or `/`)
   
2. **Processing:** Based on the operator provided by the user, the calculator performs the corresponding arithmetic operation:
   - **Addition:** Adds the two numbers.
   - **Subtraction:** Subtracts the second number from the first.
   - **Multiplication:** Multiplies the two numbers.
   - **Division:** Divides the first number by the second, unless the second number is zero, in which case an error message is displayed.

3. **Output:** The result of the operation is displayed. If the user inputs an invalid operator, an error message is displayed prompting them to try again.

## How It Was Built

This calculator was built using basic Python functions and control structures. The `input()` function is used to gather user inputs, and conditional statements (`if-elif-else`) are utilized to perform the correct arithmetic operation based on the operator input. To ensure smooth user interaction, the program checks for division by zero and alerts the user when such a case occurs.

The program structure follows a simple and intuitive design, making it easy to use, even for those with minimal experience in programming.
