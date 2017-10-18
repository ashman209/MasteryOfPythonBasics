# Filename: tempconv.py
# Author: Rick Halterman
# Last modified: August, 2011
# Converts degrees Fahrenheit to degrees Celcius
# Based on the formula found at
# https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

# Prompt user for temperature to convert and read the supplied value

degreesF = eval(input('Enter the temperature in degrees F°: '))
# Perform the conversion
degreesC = 5/9*(degreesF - 32)
# Report the result
print(degreesF, "degrees F =", degreesC, 'degrees C')
