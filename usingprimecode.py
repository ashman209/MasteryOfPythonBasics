# 9.75 Listing 8.6: usingprimecode.py
from primecode import is_prime

def main():
    num = int(input("Enter an integer: "))
    if is_prime(num):
        print(num, "is prime")
    else:
        print(num, "is NOT prime")