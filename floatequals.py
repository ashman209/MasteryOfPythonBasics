# 8-69 Listing 7.16 floatequals.py
from math import fabs

# equals (a, b, tolerance)
#   Returns true if a = b or |a - b| < tolerance.
#   If a and b differ by only a small amount (specified by tolerance),
#   a and b are considered 'equal'.
#   Useful to account for floating-point round-off error.
#   The == operator is checked first since some special floating-point
#   values such as floating-point infinity require an exact equality check!
def equals(a, b, tolerance):
    return a == b or fabs(a- b) < tolerance

# Try out the equals function
def main():
    i = 0.0
    while not equals(i, 1.0, 0.001):
    # The 3rd parm specifies how close the first two parms must be to be considered 'equal'.
        print("i =", i)
        i += 0.1

main()
