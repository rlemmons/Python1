#!/usr/bin/env python3
import sys

def verify_pin(pin):
    """

    """
    if pin == '1234':
        return True
    else:
        return False

def lock():
    """

    """
    print("Your card has been locked out")
    exit(1)


# Main function
def GetInput():
    """
    Test 1  Function
    """
    tries = 0
    while tries < 4:
        pin = input('Enter your pin: ')
        if verify_pin(pin):
            print("Your pin is correct")
            return True
        else:
            if len(pin) != 4:
                print("Invalid PIN length. Correct format is: <8372>")
                tries += 1
                if tries == 3:
                    lock()

            elif pin.isnumeric() == True:
                print("Your PIN is incorrect")
                tries += 1
                if tries == 3:
                    lock()

            else:
                print("Invalid Pin character. Correct format is: <9876>")
                tries += 1
                if tries == 3:
                    lock()


if __name__ == "__main__":
	# Call Main
	GetInput()

	exit(0)
