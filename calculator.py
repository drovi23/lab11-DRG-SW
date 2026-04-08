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
=======
# First example
import math
def square_root(a):
    if a < 0:
        raise ValueError

def hypotenuse(a,b):
    math.hypot(a,b)


def multiply(a, b):
    return a * b


def exponent(a,b):
    a**b
