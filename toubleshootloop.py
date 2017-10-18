# File toubleshoot.py
print("Help! My computer doesn't work!")
done = False    # Not done initially
while not done:
    print("Does the computer make any sounds (fans, etc.)")
    choice = input("or show any lights? (y/n):")
    # The troubleshooting control logic
    if choice == 'n':       # The computer does not have power
        choice = input("Is it plugged in? (y/n):")
        if choice == 'n':   # If is not plugged in, plug it in
            print("Plug it in.")
        else:               # It is plugged in
            choice = input("Is the switch in the \"on\" position? (y/n):")
            if choice == 'n':   # The switch is off, turn it on!
                print("Turn it on.")
            else:           # The swith is on
                choice = input("Does the computer have a fuse? (y/n):")
                if choice == 'n':   # No fuse
                    choice = input("Is the outlet OK? (y/n):")
                    if choice == 'n':   # Fix outlet
                        print("Check the outlet's circuit ")
                        print("breaker or fuse.  Move to a")
                        print("new outlet, if necessary. ")
                    else:           # Beats me!
                        print("please consult a service technician.")
                        done = True # Nothing else I can do
                else:               # Check fuse
                    print("Check the fuse. Replace if ")
                    print("necessary.")
    else:           # The computer has power
        print("Please consult a service technician.")
        done = True  # Nothing else I can do