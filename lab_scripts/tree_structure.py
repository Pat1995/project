#!/usr/bin/python3
import os

path = '/home/pythonml'
for root, dirs, files in os.walk(path):
	for f in files:
        	print(" " + os.path.join(root, f))
