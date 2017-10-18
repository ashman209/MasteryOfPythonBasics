# File better-die.py
from random import randrange
# show_die (spots)
#   Draws a picture of a die with number of spots

#       indicated spots is the number of spots one the top face of the die
def show_die(spots):
    print("+-------+")
    if spots == 1:
        print("|       |")
        print("|   *   |")
        print("|       |")
    elif spots == 2:
        print("| *     |")
        print("|       |")
        print("|     * |")
    elif spots == 3:
        print("| *     |")
        print("|   *   |")
        print("|     * |")
    elif spots == 4:
        print("| *   * |")
        print("|       |")
        print("| *   * |")
    elif spots == 5:
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
    elif spots == 6:
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
    else:
        print(" **** Error: illegal die spots **** ")
    print("+-------+")

# roll
#   Returns a pseudorandom number in the range of 1 through 6
def roll():
    return randrange(1, 6)

# main
#   Simulates the roll of a die three times
def main():
    # Roll the die three times
    for i in range(0, 3):
        show_die(roll())

main()  # Run the program!!!
# See main is oblivious to the details of the pseudorandom number generation function.
# And main is not responsible for drawing the die!
# These two important components are now in functions, so they can be perfected
# independently from main.
# Note how the result of the call to "roll" is passed directly as an argument to "show_die"
# => get random value 1-6 and show the die...... bang!