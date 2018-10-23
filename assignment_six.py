import random


def birthday_list():
    birthdays = []
    for x in range(23):
        birthdays.append(random.randint(1, 365))
    print(birthdays)
    return birthdays


def list_check(birthdays):
    check_birthdays = set(birthdays)
    if len(check_birthdays) < len(birthdays)        






dates = birthday_list()
list_check(dates)
