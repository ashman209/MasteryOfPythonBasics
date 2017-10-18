# File printprimes.py
max_value = eval(input('Display primes up to what value? '))
value = 2                       # The smallest prime number
                                # Definition: A Prime Number can be divided evenly
                                # only by 1, or itself.
                                # And it must be a whole number greater than 1
while value <= max_value:       # See if value is prime
    is_prime = True             # Try all possible factors from 2 to value -1
    trial_factor = 2
    while trial_factor < value:
        if value % trial_factor == 0:
            is_prime = False;   # Found a factor
            break               # No need to continue; it is NOT prime!
        trial_factor += 1       # Try the next potential factor
    if is_prime:
        print(value, end=' ')   # Display the prime number
    value += 1                  # Try the next potential prime number
print()                         # Move the cursor down to the next line - carriage return!
# Q&A
# 1.) Why does 2 work then?
# 2 is not less than 2!  So the inner loop is skipped is_prime
# is not changed from true and so 2 is printed!  This is correct
# because 2 is the smallest prime number and the only even one to boot!
# 2.) What about less than 2?  The while condition ensures that values <2 are not considered!
# Thus the body of the while will never be entered, only the newline is printed, no numbers.
# 3.) Is the inner loop guaranted to always terminate?
# in order to enter the inner loop, the trial_factor must be less than value
# And value does not change anywhere in the loop.
# trial_factor is not modified anywhere in the if statement w/in the loop.
# And it is incremented w/in the loop immmediately after the if statement.
# Thus trial_factor is incremented during each iteration of the loop.
# Eventually, trail_factor = value and the loop terminates!
# 4.) Is the outer loop guaranteed to always terminate?
# To enter the body of the outer loop, value must be less than or equal to max_value.
# max_value does not change anywhere in the loop.
# value is increased in the last statement w/in the body of the outer loop and value
# is not modified anywhere else.
# Since inner loop is guaranteed to terminate as shown in 3 above, eventually
# value will exceed max_value and the loop will end.