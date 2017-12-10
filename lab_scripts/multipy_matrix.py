#!/usr/bin/python3
import numpy as np

firstMatrix = np.random.rand(8,8)
secondMatrix = np.random.rand(8,8)

res = [[0 for col in range(len(secondMatrix[0]))] for row in range(len(firstMatrix))]
for x in range(len(firstMatrix)):
    for y in range(len(secondMatrix)):
        for z in range(len(firstMatrix)):
            res[x][y] += firstMatrix[x][z] * secondMatrix[z][y]
        
print(res)    



