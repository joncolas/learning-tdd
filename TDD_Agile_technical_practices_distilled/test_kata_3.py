from kata_3 import (
    getFibonacciNumber
)

""" TDD_Agile_technical_practices_distilled: kata 3 """

""" Write some code to generate the Fibonacci number for the nth position. """
""" Example: int Fibonacci(int position). The first Fibonacci numbers in the"""
""" sequence are: 1, 1, 2, 3, 5, 8, 13, 21 """

""" What is a fibonacci number ?"""
""" A fibonnacci number is a number generated with the sum of the previous 2 numbers starting by 0 and 1 """
""" IN EXAMPLE """
""" position 1 - 1 """
""" position 2 1=1 """
""" position 3 1+1=2 """
""" position 4 1+2=3 """
""" position 5 2+3=5 """
""" position 6 3+5=8 """
""" position 7 5+8=13 """
""" position 8 8+13=21 """


def test_return_one_when_we_pass_first_fibonacci_position():
    position = 1

    secuence_number = getFibonacciNumber(position)
    assert secuence_number == 1


def test_return_one_when_we_pass_second_fibonacci_position():
    position = 2

    secuence_number = getFibonacciNumber(position)
    assert secuence_number == 1


def test_sum_previous_two_fibonacci_numbers_when_we_ask_for_any_position_greater_than_two():
    position = 3
    previous_position = 2
    before_previous_position = 1

    previous_fibonacci_secuence_number = getFibonacciNumber(previous_position)
    before_previous_fibonacci_secuence_number = getFibonacciNumber(before_previous_position)
    secuence_number = getFibonacciNumber(position)

    assert secuence_number == previous_fibonacci_secuence_number + before_previous_fibonacci_secuence_number
