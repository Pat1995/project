#!/usr/bin/python3

cipherCode = input("Cipher code: \n")

counter = 3

while counter > 0:
    inputCode = input("Enter code: \n")
    if cipherCode == inputCode:
        print("Cipher unlocked")
        break
    counter -=1
    print("Wrong code ", counter, "left")
