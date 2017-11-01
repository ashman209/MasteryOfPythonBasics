# 9.74 Listing 8.2 factorialtest.py
# factorial(n)
#   Computes n!
#   Returns the factorial of n
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    # Try out the factorial function
    print(" 0! = ", factorial(0))
    print(" 0! = ", factorial(1))
    print(" 0! = ", factorial(6))
    print(" 0! = ", factorial(10))

main()

