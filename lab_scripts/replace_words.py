#!/usr/bin/python3

with open('file1.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('i', 'oraz')
filedata = filedata.replace('oraz', 'i')
filedata = filedata.replace('nigdy', 'prawie')
filedata = filedata.replace('dlaczego', 'nigdy')

# Write the file out again
with open('file1.txt', 'w') as file:
  file.write(filedata)

