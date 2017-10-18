# File alternatedivision.py
dividend, divisor = eval(input("Please enter two numbers to divide: "))
# If possible, divide them and report the result
if divisor !=0:
    quotient = dividend/divisor
    print(dividend, '/', divisor, "=", quotient)
print('Program Finished')