# File definite2.py
# Here we cannot predict how many times the loop will repeat
# But once the program obtains the user's input and
# before the start of execution, we know the number of iterations
# the while loop will perform.
n = 1
stop = int(input())
while n <= stop:
    print(n)
    n += 1