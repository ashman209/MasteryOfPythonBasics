# 10-82 Listing 9.16: prefixsuffix.py
a = [1, 2, 3, 4, 5, 6, 7, 8]
print("Prefixes of", a)
for i in range(0, len(a) + 1):
    print("<", a[0:i], ">", sep=" ")
print("----------------------")
print("Suffixes of", a)
for i in range(0, len(a) + 1):
    print("<", a[i:len(a) + 1], ">", sep=" ")
