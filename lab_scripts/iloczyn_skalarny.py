#!/usr/bin/python3

aList = [1,2,12,4]
bList= [2,4,2,8]
suma = 0;
for (a,b) in zip(aList, bList):
    suma += a * b

print(suma)
