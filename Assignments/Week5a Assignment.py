'''
Problem Statement
You are building a small Python utility that demonstrates your understanding of core data structures
and built-in functions covered in this session.

Tasks
Task 1 — Tuples Create a tuple of five city names, unpack it into five separate variables, 
and print each variable. Then try to modify the first element and handle the resulting error 
with a try-except block that prints a clear message.

Task 2 — Sets Create two sets — one for students who passed a Python test and one for students who 
passed a SQL test. Print the union, intersection, and difference (Python-only passers) using set 
operators.

Task 3 — Lists and ASCII Create a list of five integers representing ASCII values. 
Use a loop with chr() to print each integer alongside its corresponding character. 
Then use ord() to retrieve and print the ASCII value of the character 'Z'.

Task 4 — Subprocess Use the subprocess module to run the shell command whoami and print the 
captured output using result.stdout.
'''
# Task 1 — Tuples
cities = ("Mumbai", "Delhi", "Chennai", "Kolkata", "Bangalore")

# Unpacking
c1, c2, c3, c4, c5 = cities

print("Task 1 Output:")
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)

# Attempt to modify tuple
try:
    cities[0] = "Pune"
except TypeError:
    print("Error: Tuples are immutable and cannot be modified.")


# Task 2 — Sets
python_pass = {"Raj", "Amit", "Neha", "Priya"}
sql_pass = {"Neha", "Priya", "Karan", "Vikas"}

print("\nTask 2 Output:")
print("Union:", python_pass | sql_pass)
print("Intersection:", python_pass & sql_pass)
print("Python Only:", python_pass - sql_pass)


# Task 3 — Lists and ASCII
ascii_values = [65, 66, 67, 68, 69]

print("\nTask 3 Output:")
for val in ascii_values:
    print(val, "->", chr(val))

# ASCII of 'Z'
print("ASCII of 'Z':", ord('Z'))


# Task 4 — Subprocess
import subprocess

print("\nTask 4 Output:")
result = subprocess.run(["whoami"], capture_output=True, text=True)
print("Current User:", result.stdout.strip())