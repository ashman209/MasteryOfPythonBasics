# 8-62 Listing 7.8 parampassing.py
# Illustrate the consequences of passing an immuttype to a function
# The variable x in main is unaffected by increment because x
# references an integer and all integers are immutable!
def increment(x):
    print("Beginning execution of increment, x=", x)
    x += 1  # Increment x
    print("Ending execution of increment, x =", x)

def main():
    x = 5
    print("Before increment, x =", x)
    increment(x)
    print("After increment, x =", x)

main()