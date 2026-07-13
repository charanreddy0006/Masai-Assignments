
# Problem Statement:
# A logistics company wants to record the daily number of packages handled at five warehouses, 
# read the data back, and compute basic statistics on it using NumPy.

# Tasks
# Task 1 — Create and Write to a File Create a file called warehouse_data.txt using 
# the with statement. Write the following five values into it, one per line: 120, 85, 200, 95, 150.
# In a comment, explain what would happen if 'w' mode were replaced with 'a' mode on a second run of the same script.

# Task 2 — Read the File Open warehouse_data.txt in read mode using the with statement. 
# Read all lines into a list, strip the newline character from each, and print every value. In a comment, state which reading method you used and why it suits this task better than read() or readline().

# Task 3 — Create a NumPy Array and Compute Statistics Convert the list of values into 
# a 1D NumPy array of integers. Print the array, its dtype, shape, and size. 
# Then print the sum, maximum, and minimum using NumPy operations. In a comment, 
# explain what would happen to the dtype if one of the values in the file were the word 'error' instead of a number.


import numpy as np
# Task 1 — Create and Write to a File
with open("warehouse_data.txt","w") as file:
    file.write("120\n")
    file.write("85\n")
    file.write("200\n")
    file.write("95\n")
    file.write("159\n")

# Task 2 — Read the File
with open("warehouse_data.txt","r") as file:
    lines=file.readlines()
cleaned_data = [line.strip() for line in lines] 

print("Values read from file:")
for value in cleaned_data:
    print(value)

# Task 3 — NumPy Array and Statistics    
# Convert list to NumPy array of integers
arr = np.array(cleaned_data, dtype=int)

print("\nNumPy Array:", arr)
print("Data Type:",arr.dtype)
print("Shape:", arr.shape)
print("Size:",arr.size)

# Compute statistics
print("Sum:",np.sum(arr))
print("Maxium:",np.max(arr))
print("Minimum:",np.min(arr))
