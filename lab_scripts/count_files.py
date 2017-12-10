#!/usr/bin/python3
import os, os.path

path = '/dev'
num_of_files = len([f for f in os.listdir(path)
                   if os.path.isfile(os.path.join(path, f))])

print("Num of files in /dev directory: " + str(num_of_files))
