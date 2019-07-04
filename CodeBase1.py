"""
The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number is found by adding up the two numbers before it.
Write a recursive method fib(n) that returns the nth Fibonacci number. n is 0 indexed, which means that in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., n == 0 should return 0 and n == 3 should return 2.
Assume n is less than 15.

"""

def fib(n):
    num1 = 0
    num2 = 1
    num3 = 0

    if n == 0:
        return 0
    if n == 1:
        return 1

    for _ in range(0, n-1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3

    return num2
