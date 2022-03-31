#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program calculates the surface area of a cube
#   with user input


def main():
    # this function calculates the numbers

    integer = int(input("Enter in the integer you wish to calculate: "))

    # process
    calculation = 6 * integer**2

    # output
    print("")
    print("{} * {} = {}²".format(6, integer, calculation))
    print("\nDone")


if __name__ == "__main__":
    main()
