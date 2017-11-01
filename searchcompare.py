# 10-90 Listing 10.5: searchcompare.py
def binary_search(lst, seek):
    '''
    Returns the index of element seek in list lst,
    if seek is present in lst.
    Returns None if seek is not an element of lst.
    lst is the lst in which to search.
    seek is the element to find.
    '''
    first = 0               # Initialize the first position in the list
    last = len(lst) - 1     # Initialize the last postition in the list
    while first <= last:
        # mid is middle position in the list
        mid = first + (last - first + 1)//2      # Note: Integer division!
        if lst[mid] == seek:
            return mid      # Found it!
        elif lst[mid] > seek:
            last = mid - 1  # Continue with the 1st half
        else:               # v[mid] < seek
            first = mid + 1 # Continue with the 2nd half
    return None             # Doh, it's not there!

def ordered_linear_search(lst, seek):
    '''Returns the index of element seek in the list lst
    if seek is present in the lst.
    lst must be in sorted order.
    Returns None if seek is not an element of lst.
    lst is the lst in which to search.
    seek is the element to find.'''
    i = 0
    n = len(lst)
    while i < n and lst[i] <= seek:
        if lst[i] == seek:
            return i        # Return position immediately
        i += 1
    return None             # Element not found

def test_searches(lst):
    from time import clock

    # Find each element using ordered linear search
    start = clock()         # Start the clock
    n = len(lst)
    for i in range(n):
        if ordered_linear_search(lst, i) != i:
            print("error")
    stop = clock()            # Stop the clock
    print("Linear elapsed time", stop - start)

    # Find each element using binary search
    start = clock()         # Start the clock
    n = len(lst)
    for i in range(n):
        if binary_search(lst, i) != i:
            print("error")
    stop = clock()            # Stop the clock
    print("Binary elapsed time", stop - start)

def main():
    SIZE = 20000
    test_list = list(range(SIZE))
    test_searches(test_list)

main()

