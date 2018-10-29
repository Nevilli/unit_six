# Liam Neville
# 9/29/18
# This program creates a random list of birthdays and checks for matches, if there are matches, they are calculated
# into a percent.


import random


def birthday_list():
    """
    This function creates the random list of birthdays
    :return: birthdays is a list of 23 values representing birthdays and is returned to be checked for matches
    """
    birthdays = []
    for x in range(23):
        birthdays.append(random.randint(1, 365))
    return birthdays


def list_check(birthdays):
    """
    This function checks the list of birthdays for matches
    :param birthdays: This is the random list of birthdays
    :return: True is returned only if there is a match
    False is returned if there is no matches
    """
# set is used below because there is a collection of values
    check_birthdays = set(birthdays)
    if len(check_birthdays) < len(birthdays):
        return True
    else:
        return False


def main():
    matches = 0
    how_many = int(input("How many times would you like to run this?"))
    for x in range(how_many):
        dates = birthday_list()
        if list_check(dates) is True:
            matches = matches + 1
    print("There were", matches, "matches out of", how_many)
    percent = matches / how_many * 100
    print("That is", percent, "percent")


main()
