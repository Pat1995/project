#!/usr/bin/python3
import numpy as np

def addM(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        res.append(row)
    return res

firstMatrix = np.random.rand(128,128)
secondMatrix = np.random.rand(128,128)

addedMatrix = addM(firstMatrix,secondMatrix)

print(firstMatrix)
print(secondMatrix)
print(addedMatrix)
