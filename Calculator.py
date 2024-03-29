
from __future__ import division
import math


def addition(a, b):
    a = int(a)
    b = int(b)
    c = b + a
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c

def division(a, b):
    a = int(a)
    b = int(b)
    c = float(b / a)
    return round(c, 9)

def square(a):
    a = int(a)
    c = a ** 2
    return c

def squareroot(a):
    a = int(a)
    c = math.sqrt(a)
    return float(format(c, '.8f'))


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot(a)
        return self.result
