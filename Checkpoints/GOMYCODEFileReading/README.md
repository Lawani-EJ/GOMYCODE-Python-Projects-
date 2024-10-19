# File Reading Checkpoint
This repository contains solutions to various file-reading tasks assigned as a checkpoint during the GOMYCODE coding bootcamp. Below is an overview of each task and what it accomplishes.

## 📝 Task Overview

### 1. Read an Entire Text File
**Description:** This function reads the entire content of a given text file and returns it. It handles scenarios where the file might not exist by returning a custom error message if the file is not found.

### 2. Read the First n Lines of a File
**Description:** This function reads the first `n` lines from a specified text file. It allows for partial file reading, which can be useful when you only need a snippet of the file's content.

### 3. Read the Last n Lines of a File
**Description:** This function retrieves the last `n` lines of a text file. It uses the `deque` collection for efficient file handling, especially with large files.

### 4. Count the Number of Words in a File
**Description:** This function counts the total number of words in a specified text file. It reads the entire file content, splits it into words, and calculates the total word count.

### 5. (Bonus) Read the Last n Lines of a File (Alternative Method)
**Description:** An alternative approach to reading the last `n` lines of a file, using the `readlines()` method. This method reads the entire file into a list and slices the last `n` elements.