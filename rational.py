# 13-100 Listing 12.2: rational.py
class Rational:
    '''Represents a rational number (fraction)'''
    def __init__(self, num, den):
        self.__numerator = num
        if den != 0:
            self.__denominator = den
        else:
            print("Attempt to make an illegal rational number")
            from sys import exit
            exit(1)         # Terminate program with an error code


    def get_numerator(self):
        '''Returns the numerator of the fraction.'''
        return self.__numerator

    def get_denomiator(self):
        '''Returns the denominator of the fraction.'''
        return self.__denominator

    def set_numerator(self, n):
        '''Sets the numerator of the fraction to n.'''
        self.__numerator = n

    def set_denomiator(self, d):
        '''Sets the denominator of the fraction to d,
        unless d is zero.  If d is zero, the method terminates
        the program with an error message.'''
        if d != 0:
            self.__denominator = d
        else:
            print("Error: zero denominator!")
            from sys import exit
            exit(1)             # Terminate program with an error code
    def __str__(self):
        '''Make a string representation of a Rational object'''
        return str(self.get_numerator()) + "/" + str(self.get_denomiator())

# Client code that uses Rational objects
def main():
    fract1 = Rational(1, 2)
    fract2 = Rational(2, 3)
    print("fract1 =", fract1)
    print("fract2 =", fract2)
    fract1.set_numerator(3)
    fract1.set_denomiator(4)
    fract2.set_numerator(1)
    fract2.set_denomiator(10)
    print("fract1 =", fract1)
    print("fract2 =", fract2)

main()
