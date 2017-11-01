# 10-89 Listing 10.3: linearsearch.py

def locate(lst, seek):
    '''Returns the index of element seek in list lst,
    if seek is present in lst.
    Returns None if seek is not an element of lst.
    lst is the lst in which to search.
    seek is the element to find.'''
    for i in range(len(lst)):
        if lst[i] == seek:
            return i            # Return position immediately
    return None
    print()