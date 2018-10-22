import random

def birthday_list():
    birthdays = []
    for x in range(23):
        birthdays.append(random.randint(1, 366))
    print(birthdays)

birthday_list()