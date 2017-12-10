#!/usr/bin/python3
import random

def bubble_sort(numsList):
	for num in range(0, len(numsList)-1):
		for i in range(num+1, len(numsList)):
			if numsList[i] > numsList[num]:
				temp = numsList[i]
				numsList[i] = numsList[num]
				numsList[num] = temp
 
numsList = random.sample(range(1000), 50)


print("Random nums: \n", numsList)

bubble_sort(numsList)

print("Sorted nums: \n",numsList)
