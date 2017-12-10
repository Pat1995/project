#!/usr/bin/python3

f = open("file.txt",'r') #dorobić pliki bo nie wiem jakie maja być podane na wejscie
lines = f.readlines()
f.close()

sie = "się"
i = "i"
oraz = "oraz"
nigdy = "nigdy"
dlaczego = "dlaczego"

newLines = []
for line in lines:
    newLines.append(' '.join([word for word in line.split() if word != sie and word != i and word != oraz and word != nigdy and word != dlaczego]))

f = open("file.txt", 'w')
for line in newLines:
    f.write("{}\n".format(line))
f.close()
