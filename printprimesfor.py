# File printprimesfor.py to short then code for printprimes*.py
max_value = eval(input('Display primes up to what value? '))
# Try values from 2 (smallest prime number) to max_value
for value in range(2, max_value + 1):
 # See if value is prime
    is_prime = True                 # Provisionally, value is prime
 # Try all possible factors from 2 to value -1
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False        # Found a factor
            break                   # No need to continue, factor is NOT prime!
 # interesting results when the following if is nested! add a TAB and see ;o)
    if is_prime:
        print(value, end=' ')       # Display the prime number
print()                             # Move cursor down to the next line.