#!/usr/bin/python3

f = open("file.txt","r")

print(f.read())

tekst = "\nZadanie 1 dotyczy operacji na pliku tj. odczyt i zapis\n"

f = open("file.txt","a")

f.write(tekst)

f.close()
