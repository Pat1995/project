#!/usr/bin/python3

class Complex:
    def __init__(self, re, im):
        self.r = re
        self.i = im
    def add(self, other):
        return Complex((self.r + other.r), (self.i + other.i))
    def subtrack(self, other):
        return Complex((self.r - other.r), (self.i - other.i))
    def multiply(self, other):
        return Complex((self.r*other.r - self.i*other.i), (self.i*other.r + self.r*self.i))
    def abs(self):
        return sqrt(self.r**2 + self.i**2)

    def prints(self):
        print("re = ", self.r, ", im = ", self.i)



x = Complex(1.0, 1.0)
y = Complex(2.0, 2.0)
x.prints()
y.prints()

print("Add")
z = x.add(y)
z.prints()

print("Subtrack")
z = x.subtrack(y)
z.prints()

print("Multiply")
z = x.multiply(y)
z.prints()



