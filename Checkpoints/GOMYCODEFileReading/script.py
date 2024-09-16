# Read an Entire Text File 
def read_entire_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not Found."
    
print(read_entire_file("Example3.txt"))


# Read the first n lines of a file 
def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = [file.readline() for _ in range(n)]
        return ''.join(lines)
    except FileNotFoundError:
        return "File not found."

print(read_first_n_lines("Example3.txt", 1))


# Read the last n lines of a file 
from collections import deque

def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = deque(file, n)
        return ''.join(lines)
    except FileNotFoundError:
        return "File not found."
    
print(read_last_n_lines("Example3.txt", 1))

# Count the number of words in a file 
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        words = content.split()
        return len(words)
    except FileNotFoundError:
        return "File not found."
print(count_words_in_file("Example3.txt"))
file_path = 'Example3.txt'
print(f"The Number of words Present: {count_words_in_file(file_path)}")


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
print(read_last_n_lines_alt(file_path, n))
