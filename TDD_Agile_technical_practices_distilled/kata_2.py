#!/usr/bin/env python


def isLapYear(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        return True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    return False


def main():
    year = int(input('Enter a valid YEAR:'))
    return isLapYear(year)


if __name__ == '__main__':
    print(main())
