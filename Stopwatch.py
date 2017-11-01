# 13-102 Listing 12.3: Stopwatch.py
from time import clock

class Stopwatch:
    def __init__(self):
        self.reset()

    def start(self):                    # Start the timer
        if not self.__running:
            self.__start_time = clock()
            self.__running = True       # The clock is now running
        else:
            print("Stopwatch already running")

    def stop(self):                     # Stop the timer
        if self.__running:
            self.__elapsed += clock() - self.__start_time
            self.__running = False      # The clock is stopped
        else:
            print("Stopwatch is NOT running")

    def reset(self):                    # Reset the timer
        self.__start_time = self.__elapsed = 0
        self.__running = False

    def elapsed(self):                  # Reveal the elapsed time
        if not self.__running:
            return self.__elapsed
        else:
            print("Stopwatch must be stopped to display the time elapsed")
            return None
        