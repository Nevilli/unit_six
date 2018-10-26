import random


def birthday_list():
    birthdays = []
    for x in range(23):
        birthdays.append(random.randint(1, 365))
    return birthdays


def list_check(birthdays):
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
    print("There were", matches, "matches")


main()
