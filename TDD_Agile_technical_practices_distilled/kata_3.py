#!/usr/bin/env python


def getFibonacciNumber(position):
    if position >= 1 and position <= 2:
        return 1
    else:
        return getFibonacciNumber(position - 1) + getFibonacciNumber(position - 2)


def main():
    position = int(input('Enter a position to get fibonacci Number(valid positions are integers between 1 and infinite): '))
    return getFibonacciNumber(position)


if __name__ == '__main__':
    print(main())
