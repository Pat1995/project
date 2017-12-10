#!/usr/bin/python3
import math

separator = ' '
a,b,c = input("Enter a,b,c of ax^2 + bx + c = 0: \n").split(separator)

a = float(a)
b = float(b)
c = float(c)

delta = math.pow(b, 2)-(4*a*c)

try:
	sqrt_delta = math.sqrt(delta)
except ValueError:
	print("Enter 3 valid numbers")

if sqrt_delta > 0:
	x1 = (-b-sqrt_delta)/(2*a)
	x2 = (-b+sqrt_delta)/(2*a)
	print("x1: " + str(x1))
	print("x2: " + str(x2))
elif sqrt_delta == 0:
	x0 = -b/(2*a)
	print("x0: " + str(x0))
else:
	print("Square root do not exist")
