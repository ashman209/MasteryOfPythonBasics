# 8-70 Listing 7.17 squarerootfunction.py
# Computes the approximate square root of val
# val is a number
def square_root(val):
    root = 1.0                          # Compute a provisional square root
    diff = root*root - val              # How far off is our provisional root?

    # Loop until the provisional root is close enough to the actual root!
    while diff > 0.00000001 or diff < -0.00000001:
        root = (root + val/root) / 2    # Compute the NEW provisional root.
        diff = root*root - val          # How far off is our provisional root?
    return root

def main():
    # Get value from the user
    num = float(input("Enter number: "))
    # Report square root
    print("Square root of", num, "=", square_root(num))

main()
