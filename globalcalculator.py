# 9.72 Listing 8.1: globalcalculator.py (it's a doozy!)
# help_screen
#   Displays information about how the program works
#   Accepts no parameters and returns nothing
def help_screen():
        print("Add: Adds two numbers")
        print("Subtract: Subtracts two numbers")
        print("Print: Displays the result of the latest operation")
        print("Help: Displays this help screen")
        print("Quit: Exits the program")

# menu
#   Display a menu
#   Accepts no parameters
#   Returns the string entered by the user.
def menu():
    # Display a menu
    return input("=====  A)dd  S)ubtract  P)rint   H)elp   Q)uit ====")

# Global variables used by several functions
result = 0.0
arg1 = 0.0
arg2 = 0.0

# get_input
# Assigns the globals arg1 and arg2 from user keyboard input
def get_input():
    global arg1, arg2 # arg1 and arg2 are globals
    arg1 = float(input("Enter argument #1: "))
    arg2 = float(input("Enter argument #2: "))

# report
# Reports the value of the global result
def report():
    # Not assigning to result, global keyword not needed
    print(result)

# add
#   Assigns the sum of the globals arg1 and arg2 to the global variable result
def add():
    global result   # Assigning to result, global keyword needed
    result = arg1 + arg2

# subtract
#   Assigns the difference of the globals arg1 and arg2 to the global variable result
def subtract():
    global result   # Assigning to result, global keyword needed
    result = arg1 - arg2

# main
#   Runs a command loop that allows users to perform simple arithmetic.
def main():
    done = False    # Initially not done
    while not done:
        choice = menu()            # Get user's choice

        if choice == "A" or choice == "a":       # Addition
            get_input()
            add()
            report()
        elif choice == "S" or choice == "s":     # Subtraction
            get_input()
            subtract()
            report()
        elif choice == "P" or choice == "p":     # Print
            report()
        elif choice == "H" or choice == "h":     # Help
            help_screen()
        elif choice == "Q" or choice == "q":     # Quit
            done = True

main()
