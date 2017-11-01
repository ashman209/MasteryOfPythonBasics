# 9.75 Listing 8.5: primecode.py
# Contains the definition of the is_prime function
from math import sqrt

# Returns True if non-negative integer is prime;
# otherwise, return False.
def is_prime(n):
    trial_factor = 2
    root = sqrt(n)

    while trial_factor <= root:
        if n % trialfFactor == 0:    # Is trialFactor a factor?
            return False;           # Yes, then return right away.
    return True;                    # Tried them all, must be prime
