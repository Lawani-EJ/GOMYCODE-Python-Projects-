# DataFrame Manipulation Checkpoint
This repository contains solutions to tasks focused on DataFrame manipulation using Pandas, as assigned for the checkpoint at GOMYCODE. Below is an overview of each task performed and what the program accomplishes.

## 📝 Task Overview

### 1. Create a DataFrame
**Description:** A DataFrame is created using the provided dictionary `exam_data` and custom labels as the index. This task showcases basic DataFrame creation and structuring in Pandas.

### 2. Display the First Three Rows
**Description:** Demonstrates the use of the `head()` method to display the first three rows of the DataFrame, which can be useful for previewing data.

### 3. Delete Rows with NaN Values
**Description:** Removes any rows containing `NaN` values from the DataFrame using the `dropna()` method. This is a common data cleaning step to ensure data quality.

### 4. Extract Specific Columns
**Description:** Extracts the 'name' and 'score' columns from the DataFrame, illustrating how to filter and display specific columns of interest.

### 5. Append a New Row
**Description:** Adds a new row labeled 'k' with values for a new entry (name: "Suresh", score: 15.5, attempts: 1, qualify: "yes"). This demonstrates how to append data to an existing DataFrame.

### 6. Delete a Column
**Description:** Deletes the 'attempts' column from the DataFrame using the `drop()` method. This is useful for removing unnecessary data from a DataFrame.

### 7. Add a New Column Based on Conditions
**Description:** Adds a 'Success' column to the DataFrame, with values set to 1 if the 'score' is higher than 10, otherwise set to 0. This illustrates the use of conditional logic to derive new insights from the data.

### 8. Save the DataFrame to a CSV File
**Description:** The modified DataFrame is saved to a CSV file named `Data.csv`, demonstrating how to export data from a DataFrame for external use.