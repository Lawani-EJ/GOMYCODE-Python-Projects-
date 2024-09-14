# Read an Entire Text File 
def read_enitre_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "FIle not Found."
    
print(read_enitre_file("Example3.txt"))


# Read the first n lines of a file 
def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = [file.readline() for _ in range(n)]
        return ''.join(lines)
    except FileNotFoundError:
        return "File not found."

print(read_enitre_file("Example3.txt"))

# Read the last n lines of a file 
from collections import deque

def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = deque(file, n)
        return ''.join(lines)
    except FileNotFoundError:
        return "File not found."
    
print(read_enitre_file("Example3.txt"))

# Count the number of words in a file 
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        words = content.split()
        return len(words)
    except FileNotFoundError:
        return "File not found."

# Example usage:
file_path = 'Example3.txt'
print(f"Number of words: {count_words_in_file(Example3.txt)}")


# (Bonus) Read the last n lines of a file (Alternative method) 
def read_last_n_lines_alt(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return ''.join(lines[-n:])
    except FileNotFoundError:
        return "File not found."

# Example usage:
file_path = 'Example3.txt'
n = 5
print(read_last_n_lines_alt(Example3.txt, n))