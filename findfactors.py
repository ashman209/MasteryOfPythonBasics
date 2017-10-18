# File findfactors.py
# List the factors of the integers 1 ... MAX
MAX = 20                        # MAX is 20
n = 1                           # Start with 1
while n <= MAX:                 # Do not go past MAX
    factor = 1                  # 1 is a factor of any integer
    print(end=str(n) + ': ')    # Which integer are we examining?
    while factor <= n:          # Factors are <= the number
        # print('factor =', factor, 'n=', n) # (added later) Let's see values before
                                # going into the inner loop!
                                # Comment line 9 to see without print check-ups
        if n % factor == 0:     # Test to see if factor is a factor of n
            print(factor, end=' ')  # If so, display it
        factor += 1         # Try the next number.
                            # TAB line 11 +/- in/out of if to see infinite loop!
    print()                     # Move to the next line for next n (number)
    n += 1

    # This will freeze up or hang ignoring any user input
    # except/until the key sequence Ctl+C on most systems
    # interrupts and terminates the running program!