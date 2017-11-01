# 9.76 Listing 8.8: docprime.py
'''
Contains the definition of the is_prime function
'''
from math import sqrt

def is_prime(n):
    '''
    Returns True if non-negative integer n is prime;
    otherwise, return false
    '''
    trial_factor = 2
    root = sqrt(n)

    while trial_factor <= root:
        if n % trialfFactor == 0:   # Is trialFactor a factor?
            return False;           # Yes, then return right away.
    return True;                    # Tried them all, must be prime