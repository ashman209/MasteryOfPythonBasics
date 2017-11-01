# 12-96 Listing 11.5: printcharacters.py
s = "ABCDEFGHBCDIJK"
print(s)
for i in range(len(s)):
    print("[", s[i], "]", sep="", end="")
print()         # Print newline
for ch in s:
    print("<", ch, ">", sep="", end="")
print()         # Print newline
# Adding in this later to demonstrate strings may be manipulated
# the same way similar to lists and sliced too!
print(len(s) == s.__len__())    # Prints True!
print("ABCDEFGHBCDIJKL"[2:6])   # Prints CDEF!
# And since they are immutable, element and slice assignemnts is not possible.
s1 = "ABCDEFGHBCDIJKL"
# s1[3] = "S"                     # illegal because strings are immutable
# s1[3:7] = "XYX"                 # illegal because strings are immutable
print(s1)