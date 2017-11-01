# 10-81 List Bounds, Listing 9.14: negindex.py
def main():
    data = [10, 20, 30, 40, 50, 60]

    # Print the individual elements with negative indices
    print(data[-1])
    print(data[-2])
    print(data[-3])
    print(data[-4])
    print(data[-5])
    print(data[-6])

    print("---------")

    # Print the list in reverse using negative indices
    # for i in range(-1, -len(data), -1, -1):       # This line didn't work from the example, I fixed it
    for i in range(len(data) - 1, -1, -1):
        print(data[i], end=" ")
    print()                     # Print new line

main()                          # Execute main