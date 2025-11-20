# https://github.com/aidanq06/lab11-AQ-CN
# Partner 1: Aidan Quach
# Partner 2: Claire Natanek

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def square_root(a):
    if a < 0:
        raise ValueError("Can't take square root of negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    if a < 0:
        return a
    return b - a

def multiply(a, b):
    return a * b


def logarithm(a,b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1, and argument must be positive.")
    return math.log(a, b)

def exponent(a, b):
    return a ** b


import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b/a

def log(a, b):
    if a == 0:
        raise ValueError("Logarithm base must be positive and not equal to 1, and argument must be positive.")
    elif a < 0:
        raise ValueError("Logarithm base must be positive and not equal to 1, and argument must be positive.")
    return math.log(a,b)# use math library + raise ValueError

def exp(a, b):
    return a**b




