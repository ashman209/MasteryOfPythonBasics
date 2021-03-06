# 13-99 Listing 12.1: employee.py
# Information about one employee
class EmployeeRecord:
    def __init__(self, n, i, r):
        self.name = n
        self.id = i
        self.pay_rate = r

def open_database(filename, db):
    '''
    Read employee information from a given file and store it
    in the given vector.
    Returns true if the file ld be read;
    otherwise, it returns false.
    :param filename:
    :param db:
    :return:
    '''
    # Open file to read - interesting in doc above it auto-added last 3 lines! nice
    lines = open(filename)
    for line in lines:
        name, id, rate = eval(line)
        db.append(EmployeeRecord(name, id, rate))
    lines.close()
    return True

def print_database(db):
    '''Display the contents of the database'''
    for rec in db:
        print(str.format("{:>5}  {:<10}  {:>6.2f}", \
                         rec.id, rec.name, rec.pay_rate))

def less_than_by_name(e1, e2):
    '''Returns true if e1's name is less than e2's'''
    return e1.name < e2.name

def less_than_by_id(e1, e2):
    '''Returns true if e1's id is less than e2's'''
    return e1.id < e2.id

def less_than_by_pay(e1, e2):
    '''Returns true if e1's pay_rate is less than e2's'''
    return e1.pay_rate < e2.pay_rate

def sort(db, comp):
    '''Sort the database object db ordered by the given comp function'''
    n = len(db)
    for i in range(n - 1):
        smallest = i;
        for j in range(i + 1, n):       # Might need to remove a tab here - TBD
            if comp(db[j], db[smallest]):
                smallest = j
        if smallest != i:
            db[i], db[smallest] = db[smallest], db[i]

def main():
    # Simple "database" of employees
    database = []

    # Open file to read
    if open_database("data.dat", database):
        # Print contents of the database
        print("------ Unsorted:")
        print_database(database)

        # Sort by name
        sort(database, less_than_by_name)
        print("------ Name order:")
        print_database(database)

        # Sort by ID
        sort(database, less_than_by_id)
        print("------ ID order:")
        print_database(database)

        # Sort by pay rate
        sort(database, less_than_by_pay)
        print("------ Pay order:")
        print_database(database)
    else:                           # Error, could not open file
        print("Could not open database file")

main()
