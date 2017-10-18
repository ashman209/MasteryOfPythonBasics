# File standardsuareroot.py
from math import sqrt
# Get value from the user
num = eval(input("Enter number: "))
# Compute the square root
# This is a function invocation or function call.
# This code is the calling or client code.
# sqrt function is part of a separate module (or collection of code that
# can be used in other programs.
# The import statement makes the sqrt function available for use here.
root = sqrt(num);
# (num) is the data the function needs to perform its work.
# num is the argument or parameter passed to the function.
# The function cannot change this value, it uses the variable's value to perform the computation
# Report the result
print("Square root of", num, "=", root)