import random


def birthday_list():
    birthdays = []
    for x in range(23):
        birthdays.append(random.randint(1, 365))
    print(birthdays)
    return birthdays


def list_check(birthdays):
    check_birthdays = set(birthdays)
    while True:
        if len(check_birthdays) < len(birthdays):
            print("match")
            return True
        else:
            print("no matches")
            return False


def main():
    matches = 0
    dates = birthday_list()
    list_check(dates)
    if list_check is True:
        matches = 0 + 1
        print(matches)
