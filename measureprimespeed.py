# 7-55 measureprimespeed.py
# Now lets see how long it takes a program to count all the prime numbers to 10,000
# Using the same algorithm from 5-22 printprimesfor.py
from time import clock                  # Grab the clock function from the time package.
max_value = 10000
count = 0
start_time = clock()                    # Start the timer, snapshot 1

# Try values from 2 (smallest prime number) to max_value
for value in range(2, max_value + 1):   # See if value is prime
    is_prime = True                 # Provisionally, value is prime
    # Try all possible factors from 2 to value -1
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False        # Found a factor
            break                   # No need to continue, factor is NOT prime!
 # interesting results when the following if is nested! add a TAB and see ;o)
    if is_prime:
        count += 1                  # Count the prime number TALLY HO!
print()                             # Move the cursor down to the next line.
elapsed = clock() - start_time      # Stop the timer Bubba
print("Count:", count, " Elapsed time:", elapsed, "sec")
# My run
# Count: 1229  Elapsed time: 0.6167571504082848 sec