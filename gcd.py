# 9.74 Listing 8.4 gcd.py
# gcd(m, n)
#   Based on one of the oldest algorithms known!  c.300 BC
#   Uses Euclid's method to compute
#   the greatest common divisor
#   aka greatest common factor of m and n.
#   Returns the gcd of m and n.
def gcd(m, n):
    if n == 0:
        return m
    else:
        return(n, m % n)

def iterative_gcd(num1, num2):
    # Determin the smaller of num1 and num2
    min = num1 if num1 < num2 else num2
    # 1 is definitiely a common factor to all integers
    largestFactor = 1;
    for i in range(1, min + 1):
        if num1 % 1 == 0 and num2 % i == 0:
            largestFactor = i # Found larger factor
        return largestFactor

def main():
    # Try out the gcd function
    for num1 in range(1, 101):
        for num2 in range(1, 101):
            print("gcd of", num1, "and", num2, "is", gcd(num1, num2))
main()
