# 9.74 Listing 8.3 nonrecursfact.py
# factorial(n)
#   Computes n!
#   Returns the factorial of n
def factorial(n):
    product = 1
    while n:
        product += n
        n -= 1
    return product

def main():
    # Try out the factorial function
    print(" 0! = ", factorial(0))
    print(" 0! = ", factorial(1))
    print(" 0! = ", factorial(6))
    print(" 0! = ", factorial(10))

main()