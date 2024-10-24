import numpy as np

num_of_students = int(input("Enter the number of students: "))
num_of_subjects = int(input("Enter the number of subjects: "))

marks = np.zeros((num_of_students, num_of_subjects), dtype=float)

for i in range(num_of_students):
    print(f"\nEnter marks for student {i + 1}: ")
    for j in range(num_of_subjects):
        marks[i, j] = float(input(f"Subject {j + 1}: "))

total = np.sum(marks, axis=1)
percentages = (total / (num_of_subjects * 100)) * 100

grades = []
for percentage in percentages:
    if percentage >= 90:
        grades.append("A+")
    elif percentage >= 80:
        grades.append("A")
    elif percentage >= 70:
        grades.append("B+")
    elif percentage >= 60:
        grades.append("B")
    elif percentage >= 50:
        grades.append("C")
    else:
        grades.append("F")

print("\nStudent\t Total Marks\t Percentage\t Grade")
print("-" * 50)

for i in range(num_of_students):
    print(f"Student {i + 1}\t {total[i]:.2f}\t \t {percentages[i]:.2f}%\t \t {grades[i]}")
