# 12-96 Listing: 11.4 stripandcount.py
# Strip leading and trailing whitespace and count substrings
s = "        ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ        "
print("[", s, "]", sep="")
s = s.strip()
print("[", s, "]", sep="")

# Count occurrences of the substring "BCD"
print(s.count("BCD"))
