# 10-81 Listing 9.13: badreverse.py
def make_list():
    '''Builds a list from input provided by the user'''
    result = []         # List to return is initially empty
    in_val = 0          # Ensure loop is entered at least once
    while in_val >= 0:
        in_val = int(input("Enter integer (-1 quits): "))
        if in_val >= 0:
            result = result + [in_val]      # Add item to list
    return result

def main():
    col = make_list()           # Print the list in reverse
    # This is incorrect because it considers the first element at col[len(col)]
    # which is one index past the end of the list.
    # for i in range(len(col), 0, -1):
    # This is the corrected for statement
    for i in range(len(col) -1, -1, -1):
        print(col[i], end=" ")
    print()

main()
