#!/usr/bin/env python3
import sys

def verify_pin(pin):
    """
    This is to verify that the input is correct
    """
    if pin == '1234':
        return True
    else:
        return False

def lock():
    """
    This locks the users card if conditions are met.
    """
    print("Your card has been blocked")
    exit(1)


# Main function
def GetInput():
    """
    Main body of program, ensures correct info, format,
    and counts down the number of tries
    """
    tries = 0
    while tries < 4:
        pin = input('Enter your pin: ')
        if verify_pin(pin):
            print("Your pin is correct")
            return True
        else:
            if len(pin) != 4: #is it the correct length
                print("Invalid PIN length. Correct format is: <8372>")
                tries += 1
                if tries == 3:
                    lock()

            elif pin.isnumeric() == True: # is the pin a number
                print("Your PIN is incorrect")
                tries += 1
                if tries == 3:
                    lock()

            else: # is it a number
                print("Invalid Pin character. Correct format is: <9876>")
                tries += 1
                if tries == 3:
                    lock()


if __name__ == "__main__":
	# Call Main
	GetInput()

	exit(0)
