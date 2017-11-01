# 13-104 Listing 12.7: countingStopwatch.py
from Stopwatch import (Stopwatch)           # Inherit some/all from this class

class CountingStopwatch (Stopwatch):        # Define new class plus this stuff!
    '''Thus the single line says inherit everything from parent.  And we'll
    have start, stop, reset and elapsed methods to leverage here.
    Superclass AKA base class.  This class is a subclass or a derived class.'''

    def __init__(self):
        # Allow superclass to do its initialization of the
        # inherited fields
        super(CountingStopwatch, self).__init__()
        # Set number of starts to zero, this is the NEW field not found in parent
        self.__count = 0

    def start(self):
        # Let superclass do its start code
        super(CountingStopwatch, self).start()
        # Count this start message
        self.__count += 1

    def reset(self):
        # Let superclass reset the inherited fields
        super(CountingStopwatch, self).reset()
        # Reset new field
        self.__count = 0

    def count(self):
        return self.__count