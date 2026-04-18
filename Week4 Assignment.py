'''Assignment: Python Functions and Lists

You are building a simple marks analysis utility. Complete the following tasks in order.

Task 1. Write a function calculate_total(marks) that accepts a list of marks and returns their sum.

Task 2. Write a function calculate_average(marks) that calls calculate_total() and returns the average.

Task 3. Write a function get_grade(average) that returns "A" if average > 90, "B" if average > 75, and "C" otherwise.

Task 4. Write a function display_report(marks) that calls all three functions above and prints:

Total: <value>
Average: <value>
Grade: <value>
Task 5. Add a docstring to each function describing what it does.

Test your solution with the list [88, 76, 95, 60, 82].
'''
def calculate_total(marks):
    """
    Calculates the total sum of all marks in the list.
    
    Parameters:
    marks (list): A list of numerical marks.
    
    Returns:
    int/float: Total sum of marks.
    """
    return sum(marks)


def calculate_average(marks):
    """
    Calculates the average of marks by calling calculate_total().
    
    Parameters:
    marks (list): A list of numerical marks.
    
    Returns:
    float: Average of marks.
    """
    total = calculate_total(marks)
    return total / len(marks)


def get_grade(average):
    """
    Determines the grade based on the average marks.
    
    Parameters:
    average (float): The average marks.
    
    Returns:
    str: Grade ("A", "B", or "C").
    """
    if average > 90:
        return "A"
    elif average > 75:
        return "B"
    else:
        return "C"


def display_report(marks):
    """
    Displays the total, average, and grade by calling other functions.
    
    Parameters:
    marks (list): A list of numerical marks.
    """
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)
    
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")


# Test the solution
marks_list = [88, 76, 95, 60, 82]
display_report(marks_list)