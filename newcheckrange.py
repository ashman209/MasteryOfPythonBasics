# File newcheckrange.py
value = eval(input("Please enter an integer value in the range 0...10: "))
if value >= 0 and value <=10:   # Only one, more complicated check
    print("In range")
print("Done")
# The above can be even further reduced to "0 <= value <= 10"


