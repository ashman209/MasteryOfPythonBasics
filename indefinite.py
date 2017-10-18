# File indefinite.py
# Here we cannot predict at any point during the loops execution
# how many iterations the loop will perform.  The value to match (999)
# is known before and during the loop, but the variable can be anything
# the user enters.  'For' this, Python provides the for statement!
done = False                    # Enter the loop at least once
while not done:
        entry = eval(input())   # Get value from user
        if entry == 999:        # Did the user provide the magic number?
            done = True         # If so, get out
        else:
            print(entry)        # If not, print and continue
