from math import *

def conv(num, from_sys, to_sys):
    num = int(num, from_sys)
    if to_sys == 2:
        print(bin(num).replace("0b", ""))
    elif to_sys == 8:
        print(oct(num).replace("0o", ""))
    elif to_sys == 10:
        print(num)
    elif to_sys == 16:
        print(hex(num).replace("0x", ""))
    return

def inp():
    '''    2 - Binary
    8 - Octal
    10 - Decimal
    16 - Hexadecimal'''
    num = input("Write a number you want to convert: ")

    print("\nWhat number system would you like to convert from?")
    print(inp.__doc__)
    from_sys = input()

    print("\nWhat number system would you like to convert from?")
    print(inp.__doc__)
    to_sys = input()
    conv(num, int(from_sys), int(to_sys))

def cont():
    inp()
    while True:
        if input("Would you like to continue? (y/n): ").lower() == "y":
            inp()
        else:
            return

cont()