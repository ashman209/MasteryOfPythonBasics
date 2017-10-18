# File usingsqrt.py
# This program shows the various ways the sqrt function can be callled (used)
from math import sqrt
x = 16
# Pass a literal value and display the result
print(sqrt(16.0))
# Pass a variable and display the result
print(sqrt(x))
# Pass an expression
print(sqrt(2 * x - 5))
# Assign result to variable
y = sqrt(x)
print(y)
# Use the result in an expression
y = 2 * sqrt(x + 16) - 4
print(y)
# Use the result as an argument to a functional call
# Computes sqrt of 256 = 16 and again = 4
y = sqrt(sqrt(256.0))
print(y)
print(sqrt(int('45')))
