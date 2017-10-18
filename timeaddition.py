# 7-55 File: timeaddition.py
# Measure the time it takes for a Python program
# to add up all the integers from 1 to 100,000,000.
from time import clock
sum = 0                             # Initialize the sum accumulator
start = clock()                     # Start the stopwatch
for n in range(1, 100000001):      # Sum the numbers
    sum += n
elapsed = clock() - start           # Stop the stopwatch
print("sum:", sum, "time:", elapsed) # Report the results
# My run
# One hundred million = sum: 5000000050000000 time: 11.932587163205238