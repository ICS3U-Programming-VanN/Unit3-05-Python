#!/usr/bin/env python3
# Created by: Van Nguyen
# Created on: October 11, 2022
# This program asks the user for a number and then display
# the corresponding month


# Function that returns the month that the user inputs (in number form)
def associate_month(month):
    months = {
        1: "{} represents January.".format(month),
        2: "{} represents February.".format(month),
        3: "{} represents March.".format(month),
        4: "{} represents April.".format(month),
        5: "{} represents May.".format(month),
        6: "{} represents June.".format(month),
        7: "{} represents July.".format(month),
        8: "{} represents August.".format(month),
        9: "{} represents September.".format(month),
        10: "{} represents October.".format(month),
        11: "{} represents November.".format(month),
        12: "{} represents December.".format(month),
    }

    # If the user enters an invalid number
    return months.get(month, "Error. {} does not represent a month.".format(month))


def main():
    # Displays Instructions
    print("Please a number that corresponds to a month (ex. 3 for March)")

    # Asks user to enter a number that corresponds to a month
    user_month = int(input("Enter a Number (1-12): "))

    # Displays the month of the user's number
    print(associate_month(user_month))


if __name__ == "__main__":
    main()
