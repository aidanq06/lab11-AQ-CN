import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def square_root(a):
    if a < 0:
        raise ValueError("Can't take scquare root of negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b): 
    return a + b

def subtract(a, b,):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ValueError("Cannot divide by zero.")
    return b / a

def logarithm(a,b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1, and argument must be positive.")
    return math.log(a, b)

def exponent(a, b):
    return a ** b





