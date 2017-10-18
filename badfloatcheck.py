# 8-69 Listing 7.15: badfloatcheck.py
def main():
    # Count to ten by tenths
    i = 0.0
    while i != 1.0:
        print("i =", i)
        i += 0.1
        # It never ends!  endless loop
        # It needs to be stopped ctrl+c or abended
        # When comparing two float numbers x and y
        # We must determine if the absolute value of their
        # difference is small enough to accept and move on
        # example |x-y| < 0.00001
main()
