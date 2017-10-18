# 8-68 Listing 7.13 File treefunc.py
# tree(height)
#   Draws a tree of a given height
#   height is the number of rows used for the tree displayed
def tree(height):
    row = 0                             # First row, from the top, to draw
    while row < height:                 # Draw one row for every unit of height
        # The following loop will pring the leading spaces
        count = 0
        while count < height - row:
            print(end=" ")              # insert a space!
            count += 1
        # Now print out stars, twice the current row plus one for the center:
        #   1. number of stars on the left side of tree = current row value (left)
        #   2. exactly one star in the center of tree (middle * )
        #   3. number of stars on right side of tree = current row value (right)

        count = 0
        while count < 2*row + 1:
            print(end="*")
            count += 1
        # Move the cursor down to the next line
        print()
        # Change to the next row and away we go!
        row += 1

# main
#   Now all we need is a number/input from the user to allow
#   them to draw trees of various heights!
def main():
    height = int(input("Enter the desired height of your Christmas tree: "))
    tree(height)

main()

# Note the name 'height' is being used as a local variable and
# as a formal paramter in tree!  There is no conflict here and
# the two 'height's represent two distinct quantities.
# tree(height) uses mains height as an actual parameter and height
# happens to be the name of the formal parameter, is simply a coincidence... or was it ;o)
