![ProjectTask](/assets/CompletedCheckpointScreenshots/Screenshot%20(131).png)

# Algorithms Checkpoint
This repository contains Python implementations of various algorithms covered in the bootcamp. The scripts demonstrate sorting, searching, and other algorithmic techniques with detailed comments explaining each step. The algorithms include Binary Search, Power Calculation, Bubble Sort, Merge Sort, and Quick Sort.

## 📜 Algorithms Overview

1. **Binary Search**
   - A search algorithm that finds the position of a target value within a sorted array.
   - Uses a divide-and-conquer approach, repeatedly dividing the search interval in half.
   - Time complexity: O(log n).

2. **Power Calculation**
   - A simple function to compute the result of a number raised to a power.
   - Uses the exponentiation operator `**`.

3. **Bubble Sort**
   - A simple comparison-based sorting algorithm.
   - Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
   - Time complexity: O(n²).

4. **Merge Sort**
   - A divide-and-conquer algorithm that splits the array into halves, sorts each half, and then merges them back together.
   - Efficient for larger datasets.
   - Time complexity: O(n log n).

5. **Quick Sort**
   - Another divide-and-conquer algorithm that selects a 'pivot' and partitions the array into two sub-arrays based on the pivot.
   - Elements less than the pivot go to the left, while elements greater than the pivot go to the right.
   - Time complexity: O(n log n) on average.

## 📂 How It Works

### 1. **Binary Search**
   - Searches for a target value in a sorted array.
   - Returns `True` if the value is found and `False` otherwise.

### 2. **Power Calculation**
   - Takes two parameters and returns the first number raised to the power of the second.

### 3. **Bubble Sort**
   - Repeatedly iterates through the list, swapping adjacent elements if they are in the wrong order.
   - Continues until no more swaps are needed.

### 4. **Merge Sort**
   - Recursively divides the array into halves, sorts each half, and merges them together.

### 5. **Quick Sort**
   - Selects a pivot element and partitions the array into elements less than and greater than the pivot.
   - Recursively sorts the partitions.

## 🧪 Testing
Sample data is provided for each algorithm, with test cases showcasing how each function works:
- For **Binary Search**, arrays with different values are searched for specific elements.
- **Power Calculation** demonstrates computing different powers of base numbers.
- **Bubble Sort**, **Merge Sort**, and **Quick Sort** are tested with unsorted arrays to show the sorting process.

## ⚙ Requirements
- Python 3.x
- `requests` and `BeautifulSoup` (if using additional scripts for web scraping)

## 🔍 Usage
To run the algorithms, execute the corresponding script in a Python environment. The algorithms are self-contained, allowing for direct modification and further exploration.