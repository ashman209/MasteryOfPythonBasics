# File: moreefficientprimes.py
# To use the sqrt function to improve the efficiency in printprimes.py
# Instead of trying all the factores of n up to n-1 we need only try potential factors
# up to the square root of n.
# This uses the sqrt function to reduce the number of factors that need be considered.

from math import sqrt
max_value = eval(input('Display primes up to what value? '))
value = 2                   # The smallest prime number
while value <= max_value:   # See if value is prime
    is_prime = True         # Try all possible factors from 2 to value -1
    trial_factor = 2

    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False;   # Found a factor
            break               # No need to continue; it is NOT prime
        trial_factor += 1
    if is_prime:
            print(value, end= ' ')  # Display the number
    value += 1

print()                     # Move cursor down to the next line.