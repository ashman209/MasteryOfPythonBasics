# File datetransformer.py
month = eval(input("Please enter the month as a number (1-12): "))
day = eval(input("Please enter the day of the month: "))
# Translate month into English
if month == 1:
    print("January ", end='')
elif month == 2:
    print("February ", end='')
elif month == 3:
    print("March ", end='')
elif month == 4:
    print("April ", end='')
elif month == 5:
    print("May ", end='')
elif month == 6:
    print("June ", end='')
elif month == 7:
    print("July ", end='')
elif month == 8:
    print("August ", end='')
elif month == 9:
    print("September ", end='')
elif month == 10:
    print("October ", end='')
elif month == 11:
    print("November ", end='')
elif month == 12:
    print("December ", end='')

# Add the day
print(day, 'or', day, end='')

# Translate month into Spanish
if month == 1:
    print(" enero ", end='')
elif month == 2:
    print(" febrero ", end='')
elif month == 3:
    print(" marzo ", end='')
elif month == 4:
    print(" abril ", end='')
elif month == 5:
    print(" mayo ", end='')
elif month == 6:
    print(" junio ", end='')
elif month == 7:
    print(" julio ", end='')
elif month == 8:
    print(" agosto ", end='')
elif month == 9:
    print(" septiembre ", end='')
elif month == 10:
    print(" octubre ", end='')
elif month == 11:
    print(" noviembre ", end='')
elif month == 12:
    print(" diciembre ", end='')