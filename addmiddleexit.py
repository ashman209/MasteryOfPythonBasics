# File addmiddleexit.py copied from File addnonnegatives.py
# Allow the user to enter a sequence of non-negative
# numbers. The user ends the list with a negative
# number.  At the end the sum of the non-negative
# numbers entered is displayed.  The program prints
# zero if the user provides no non-negative numbers.

entry = 0           # Ensure the loop is#  entered
sum = 0             # Initialize sum

# Request input from the user
print("Enter numbers to sum, negative number ends list:")

while True:                 # Loop forever
    entry = eval(input())   # Get the value
    if entry < 0:           # Is number non-negative?
        break               # If so, exit the loop
    sum += entry            # Add entry to running sum
print("Sum =", sum)         # Display the sum