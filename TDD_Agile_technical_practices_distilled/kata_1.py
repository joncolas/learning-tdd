#!/usr/bin/env python


def check_divisible(number):
    if (number >= 1 and number <= 100):
        if (number % 3 == 0 and number % 5 == 0):
            return "fizzbuzz"
        elif number % 3 == 0:
            return "fizz"
        elif number % 5 == 0:
            return "buzz"
        else:
            return str(number)
    else:
        return None


def main():
    number = int(input('Enter num between 1 and 100:'))
    return check_divisible(number)


if __name__ == '__main__':
    print(main())
