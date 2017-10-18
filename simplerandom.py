# 7-56 File: simplerandom.py
from random import randrange, seed

seed(23)                                # Set random number seed
for i in range(0, 10):                 # Print 100 random numbers
    print(randrange(1, 1000), end=' ')  # Range 1....1,000
print()                                 # Print new line
# Updating just to print 10 for output
# My run
# 948 799 972 297 914 850 86 18 607 315
# Wow that repeats each time...
# This is good for DEV and TESTING when you want the program
# to executions to exhibit reproducible results!!!!

