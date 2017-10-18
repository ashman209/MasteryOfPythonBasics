# 7-55 countdown.py
# Even faster prime generator can be found!
# sleep = suspend for x seconds, print value every second on count down...
from time import sleep                  # the sleep function is in the time package
for count in range(10, -1, -1):         # Create the loop to count down
    print(count)                        # Display the counter
    sleep(1)                            # Suspend exe for 1 second, good ol' PAUSE
print("Countdown complete Mr. Powers...")
