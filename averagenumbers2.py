# 10.78 Listing 9.2: averagenumbers2.py
def main():
    sum = 0.0
    NUMBER_OF_ENTRIES = 5
    print("Please enter", NUMBER_OF_ENTRIES, "numbers:")
    for i in range(0, NUMBER_OF_ENTRIES):
        num = eval(input("Enter number " + str(i) + ":"))
        sum += num;
    print("Average:", sum/NUMBER_OF_ENTRIES)
    # Now this file can be extended to enter as many numbers as needed.
main()