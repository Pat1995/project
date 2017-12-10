#!/bin/bash

path="/home/pythonml/project"
echo "Give me a password: "
read cipher
counter=3
while [[ counter -gt 0 ]]; do
    echo "Give password to unlock cipher: "
    read pass

    if [[ pass -eq cipher ]]; then
        echo `ls -1 ..`
        break
    else
        echo "Failed to unlock"
        counter-=1
        continue  
    fi
done
