#!/usr/bin/python3
import os
import re

path = '/home/pythonml/pyt/jpg/'
for filename in os.listdir(path):
	f, ext = os.path.splitext(filename)
	if ext == ".jpg":
		os.rename(os.path.join(path,filename), os.path.join(path,f + ".png"))


	
