# File startree.py
# Get the tree height from user
height = eval(input('Enter height of tree: '))

# Draw one row for every unit of height
row = 0
while row < height:
    # Print leading spaces; as row gets bigger,
    # the number of leading spaces gets samller!
    count = 0
    while count < height - row:
        print(end=" ")
        count += 1

    # Print out stars, twice the current row plus one:
    #   1. number of stars on the left side of tree = current row value
    #   2. exactly one star in the center of tree
    #   3. number of stars on right side of tree = current row value
    count = 0
    while count < 2*row + 1:
        print(end='*')
        count += 1
    # Move cursor down to next line
    print()
    row += 1    # Consider next row