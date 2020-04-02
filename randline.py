#!/usr/bin/env python

import random
import sys
import datetime
import os


def awakeOrAsleep(time):
    if time.hour >= 9 and time.hour <= 18:
        return 1
    else:
        return 2


def timeOfDay(time):
    if time.hour <= 2 or time.hour >= 18:
        return 'evening'
    elif time.hour <= 12:
        return 'morning'
    else:
        return 'afternoon'


def todayOrTonight(time):
    if time.hour <= 4 or time.hour >= 20:
        return 'tonight'
    else:
        return 'today'


def dayOfWeek(time):
    return time.strftime('%A')


def main():
    now = datetime.datetime.now()
    eddieAwakeOrSleeping = awakeOrAsleep(now)
    columns = os.get_terminal_size().columns
    if eddieAwakeOrSleeping == 1:
        os.system('sh /Users/stefan.lachmann/Desktop/Code/Forks/eddie/welcome.sh')
        return
    else:
        lines = open(sys.argv[1]).readlines()
        name = sys.argv[2] if len(sys.argv) > 2 else 'guys'
        quote = lines[random.randrange(len(lines))].strip() % {
            'timeOfDay': timeOfDay(now),
            'todayOrTonight': todayOrTonight(now),
            'dayOfWeek': dayOfWeek(now),
            'name': name
        }
        message = quote.center(columns)
        print(message)


if __name__ == "__main__":
    main()
