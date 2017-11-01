# 14-107 Listing 13.1: pitfalls.py
# I hope the user enters a valid Python integer!
x = int(input("Please enter a small positive integer: "))
print("x =", x)
if x < 5:
    a = None
    a[3] = 2        # Using None as a populated list!
elif x < 10:
    a = [0, 1]
    a[2] = 3        # Exceeding the list's bounds
# Problems with the above:
# User enters a non-integer, results in crash with ValueError...
# User enters VALUE! < 5, program attempts to use None as a list, TypeError
# User enters 6..9, IndexError, outside the range of the list!
