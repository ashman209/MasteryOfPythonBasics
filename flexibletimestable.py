# File flexibletimestable.py
# Print a MAX x MAX multiplication table
MAX = 18
# This uses loops based on the user input!
# First, print heading
print(end="     ")
# Print the column heading numbers
for column in range(1, MAX + 1):
    print(end=" %2i " % column)
print()                                 # Go down to the next line
print(end="    ")
for column in range(1, MAX + 1):
    print(end="----")                  # Print portion of the line
print()                                 # Go down to the next line

# Print table contents
for row in range(1, MAX + 1):           # 1 <= row <= MAX, table has MAX rows
    print(end="%2i | " % row)           # Print heading for this row
    for column in range(1, MAX + 1):    # Table has 10 columns
        product = row*column;           # Compute product
        print(end="%3i " % product)     # Display product
    print()