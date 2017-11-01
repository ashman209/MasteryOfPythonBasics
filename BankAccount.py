# 13-100 Listing ??: BankAccount.py
class BankAccount:
    def __init__(self, number, ssn, name, balance):
        self.__account_number = number		# Account number
        self.__ssn = ssn					    # Social Security number
        self.__name = name				    # Customer name
        self.__balance = balance			# Funds available in the account
        self.__min_balance = 100.00		    # Balance cannot fall below this amount
        self.__active = True				# On better definition, we init the last
                # two fields with default values and allow the others
                # to be passed in as the db file is read COOL!

    def deposit(self, amount):
        '''Add funds to the account, if possible
        Return true if successful, false otherwise'''
        if self.is_active():
            self.__balance += amount
            return True     # Successful deposit
        return False        # Unable to deposit into an inactive account

    def withdraw(self, amount):
        '''Remove funds from the account, if possible
        Return true if successful, false otherwise'''
        result = False;     # Unsuccessful by default
        if self.is_active() and
            self.__balance - amount >= self.__min_balance ):
            self.__balance -= amount
            result = True    # Success
        return False

    def set_active(self, act):
        '''Activate or deactivate the account'''
        self.__active = act

    bool is_active()
    '''Is the account active or inactive'''
    return self.__active

