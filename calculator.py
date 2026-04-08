"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
#First example

import math

def add(a, b):
    return a + b
    pass
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b

def div(a,b):
    if a< 0:
        raise ZeroDivisionError

    else:
        return b/a
=======
# First example
import math
def square_root(a):
    if a < 0:
        raise ValueError

def hypotenuse(a,b):
    return math.hypot(a,b)


def multiply(a, b):
    return a * b


def exponent(a,b):
    return a**b

def log(a,b):
    if b < 0:
        raise ValueError
    else:
        return math.log(a(b))